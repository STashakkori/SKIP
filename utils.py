__author__ = 'Jacobs Space Apps Team'
__project__ = 'SpaceAppsRehearsal'

# module imports ##############
import csv
import requests
import pyowm
import sys
import gui
import json
import datetime
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import radiationCurve
import solarDataTammy
import weatherConversion
import parameters
import timeManipulation as tm
import computeNormRad
import solarData
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
###############################

planet = "earth"

class GuiCaller(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        QtCore.QCoreApplication.instance().quit()

"""
    main => the main function

    returns: none
"""
def main( ):
    #earth_forecast = get_earth_forecast_weekly( -22.57, -43.12 )
    mars_weather = get_mars_weather()
    df = pd.DataFrame()
    app = QApplication(sys.argv)        # A new instance of QApplication
    form = GuiCaller()                  # We set the form to GuiCaller object

    form.comp_button.clicked.connect(lambda: compute_power( form ))
    form.add_button.clicked.connect(lambda: add_item( form, df ))

    init_gui_components( form )
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

"""
    csv2matrix => convert a csv data file to a numpy array

    returns:
        appliance_info:
            appliance_info[0]: appliance_names
            appliance_info[1]: minimum_watts
            appliance_info[2]: maximum_watts
"""
def parse_appliances( ):
    first_row = True
    appliance_names = []
    minimum_watts = []
    maximum_watts = []
    appliance_info = []
    filename = "data/commonUsageDatabase.csv"

    with open( filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        num_rows = sum(1 for row in reader) - 1

    with open( filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        row_index = 0

        for row in reader:
            # throw out the labels; that's just for
            if first_row:
                first_row = False
                continue

            appliance_names.append( row[0] )
            minimum_watts.append( row[1] )
            maximum_watts.append( row[2] )

    appliance_info.append( appliance_names )
    appliance_info.append( minimum_watts )
    appliance_info.append( maximum_watts )
    print(" processed ", num_rows, " rows of ", filename )
    return appliance_info

def get_earth_weather( latitude, longitude ):
    api_key = "3ddc08e061550553452c39b52c1fecdb"
    weather_server = pyowm.OWM( api_key )
    weather = weather_server.weather_around_coords( latitude, longitude )[0].get_weather( )
    # weather = weather_server.weather_at_place("Huntsville,us").get_weather( )
    for method in dir( weather ):
        if callable( getattr( weather, method ) ):
            print( method )

    return weather

def get_earth_forecast_weekly( latitude, longitude ):
    api_key = "3ddc08e061550553452c39b52c1fecdb"
    req_url = "http://api.openweathermap.org/data/2.5/forecast/daily?lat="
    req_url += str( latitude )
    req_url += "&lon="
    req_url += str( longitude )
    req_url += "&appid="
    req_url += api_key
    r = requests.get( req_url, data=None, auth=None, params=None, proxies=None )
    return json.loads( r.text )

def get_earth_forecast_hourly( latitude, longitude ):

    return

def get_mars_weather( ):
    req_url = "http://marsweather.ingenology.com/v1/latest/?format=json"
    r = requests.get( req_url, data=None, auth=None, params=None, proxies=None )
    return json.loads( r.text )['report']

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%m/%d/%Y")

def init_gui_components( form ):
    # populate date text box
    today = get_date()
    form.date_box.setText( today )
    form.date_box.setReadOnly(True)

    # populate item box
    appliances = parse_appliances( )
    appliance_names = appliances[0]
    form.item_combo.addItems( appliance_names )

def get_power_fields( form ):
    if form.lat_box.text():
        latitude = form.lat_box.text()
    else:
        latitude = "0.0"

    if form.long_box.text():
        longitude = form.long_box.text()

    else:
        longitude = "0.0"

    efficiency = 0
    if form.panel_box.text():
        efficiency_box = form.panel_box.text()

    else:
        efficiency = form.panel_combo.currentText()
        if form.panel_combo.currentText() == "Monocrystalline":
            efficiency = 17.5

        if form.panel_combo.currentText() == "Galium Arsenide":
            efficiency = 34

        if form.panel_combo.currentText() == "Polycrystalline":
            efficiency = 14.5

        if form.panel_combo.currentText() == "Amorphous":
            efficiency = 14

        if form.panel_combo.currentText() == "CdTe":
            efficiency = 20

        if form.panel_combo.currentText() == "CIS/CIGS":
            efficiency = 11

    return float(latitude), float(longitude), float(efficiency)

def compute_power( form ):
    lat, long, eff = get_power_fields( form )
    print(lat)
    print(long)
    print(eff)
    earth_weather = get_earth_weather(lat, long)
    form.humid_box.setText(str(earth_weather.get_humidity()))
    form.press_box.setText(str(earth_weather.get_pressure()['press']))
    form.wind_box.setText(str(earth_weather.get_wind()['speed']))
    form.temp_box.setText(str(earth_weather.get_temperature()['temp']))
    form.wind_box_2.setText(str(earth_weather.get_wind()['deg']))
    return

def add_item( form, df ):
    # appliance stuff
    appliances = parse_appliances( )
    item_names = appliances[0]
    item_power_min = appliances[1]
    item_power_max = appliances[2]
    item_power_avg = []
    for i in range(1, len(item_names)):
        average = ( int( float( item_power_min[i] ) ) + int( float( item_power_max[i] ) ) ) / 2
        item_power_avg.append( average )
    print( item_power_avg )

    #time stuff
    start_time = 0
    stop_time = 0
    start_time = float( form.start_box.text() )
    stop_time = float( form.stop_box.text() )
    item = form.item_combo.currentText()
    watts = 0
    for i in range(1, len(item_names)):
        if item_names[i] == item:
            watts = item_power_avg[i]
            break
    df = solarDataTammy.add(item, watts, int(start_time), int(stop_time), df)
    radiationCurve.make_plot(df)
    return

if __name__ == "__main__":
    main()


#df = add('Lights',100, 17, 22, df)
#make_plot(df,  RADIATION)