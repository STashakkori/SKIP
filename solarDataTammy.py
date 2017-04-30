#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:54:08 2017

@author: tammystatham
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def energy(rad, area, efficiency):
    '''rad is the radiation on the earth's surface
       area is the m'2 area of the solar panel
       efficency of the solar panel'''

    e = rad*area*efficiency
    return e


def dailyAvg(data, avgRange):
    
    daily_averages = list()
    
    for i,d in enumerate(data):
        if (i % avgRange) == 0:
            avg_for_day = np.mean(data[i - avgRange:i])
            daily_averages.append(avg_for_day)
    return daily_averages

def dailyMax(data, maxRange):
    
    daily_maxes = list()
    
    for i,d in enumerate(data):
        if (i % maxRange) == 0:
            max_for_day = np.max(data[i - maxRange:i])
            daily_maxes.append(max_for_day)
    return daily_maxes

def solarHour(hour):
    '''INPUT: hour is the decimal number hour in the day '''
    
    w = 15*(hour - 12)
    return(w)

def atmosphere_solarIrradiance(lat, w, n):
    '''INPUT: n is the number of the day in the year
              w is the solar hour
              lat is the latitude that you are currently at'''
    
    w = np.deg2rad(w) #solar hour
    lat = np.deg2rad(lat) #latitude
    
    dec = declination(n)
    
    Gsc = 1367 #W/m^2
    Gon = Gsc*(1+0.033*np.cos(2*np.pi*n/365))
    Go = Gon*(np.cos(lat)*np.cos(dec)*np.cos(w)+np.sin(lat)*np.sin(dec))
    
    return(Go)

def unix2hourangle(unix1, unix2):
    ''' Given 2 unix times, this calculates the sidereal time
        Unix 1 is the begnning of the day
        Unix 2 is the current time'''
    
    seconds = unix2 - unix1   #difference in unix seconds
    hour = seconds/3600       #change difference into hours
    w = solarHour(hour) + 180 
    
    return(w)

def declination(n):   
    ''' Calculates the declination based on the time of the day that it is. '''
    
    dec = np.deg2rad(23.45) * np.sin(2*np.pi*(284 + n)/365) #dec
    return dec
    
def surface_solarIrradiance(lat, w, n, A):
    """INPUT: climate_type is the region and season for the area
              n is the number of the day in the year (deg)
              w is the solar hour (deg)
              lat is the latitude that you are currently at (deg)
              thetaz is the solar incidence angle off of nadir (deg)"""
    
    Gsc = 1367 #W/m^2

    w = np.deg2rad(w)
    lat = np.deg2rad(lat)
    dec = declination(n)
    
    thetaz = np.deg2rad(0)
    climate_type = 'tropical'
    if climate_type == 'tropical':
        r0 = 0.95
        r1 = 0.98
        rk = 1.02
    elif climate_type == 'midlatitude_summer':
        r0 = 0.97
        r1 = 0.99
        rk = 1.02        
    elif climate_type == 'midlatitude_summer':
        r0 = 0.99
        r1 = 0.99
        rk = 1.01 
    elif climate_type == 'midlatitude_winter':
        r0 = 1.03
        r1 = 1.01
        rk = 1.00
    else:
        print('Enter correct climate type option!')         
        
        
    ao = r0*(0.4237 - 0.00821 * (6 - A)**2)
    a1 = r1*(0.5055 + 0.00595 * (6.5 - A)**2)
    k = rk*(0.2711 + 0.01858 * (2.5 - A)**2)
    
    tb = ao + a1*np.exp(-k/np.cos(thetaz))
    td = 0.271 - 0.294*tb
    
    Gc = (tb + td)*Gsc*(1+0.033*np.cos(2*np.pi*n/365))*(np.cos(lat)*np.cos(dec)*np.cos(w) + np.sin(lat)*np.sin(dec))

    return(Gc)

def panelrad(rad, beta, lat, n):
    dec = declination(n)
    prad = (rad*np.sin(np.deg2rad(90 - lat + dec+beta))/np.sin(np.deg2rad(90 - lat + dec)))
    return prad

def add(name,watts, start_time, end_time, df):
    '''INPUT:
       name is the name of the item/appliance
       watts is the watt-h
       start_time is the nth hour of the day that the item starts
       end_time is the nth hour of the day that the item stops'''
    
    
    df['time'] = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 
                           5,   5.5, 6,   6.5,  7,  7.5, 8,   8.5, 
                           9,   9.5,
                           10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5,
                           14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 
                           18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 
                           22, 22.5, 23, 23.5, 24]) 
    
    df[name] = 0
    for i in range(start_time * 2, end_time *2 + 1):
        df[name][i] = watts

    return(df)    


def make_plot(df):
    
    bar_width = 0.45
    opacity = 0.4
    total = df.sum(1,1)-df['time']
    
    plt.bar(df['time'], total, 
            bar_width, 
            alpha=opacity)
    plt.xlabel('Hour in day')
    plt.ylabel('Watts/hour')
    plt.title('')
    plt.show()
    
    return(total)

def clear_data():
    
    df =pd.DataFrame()


if __name__ == '__main__':
        
    os.chdir('Space Apps data')
   
    PRESSURE = pd.read_csv('barometric pressure.csv', header=None)
    PRESSURE.columns = ['num','unix','date','time','value', 'ex']
    
    HUMIDITY = pd.read_csv('humidity.csv', header=None)
    HUMIDITY.columns = ['num','unix','date','time','value', 'ex']

    RADIATION = pd.read_csv('solar radiation.csv') 
    RADIATION.columns = ['num','unix','date','time','value', 'ex']
    RADIATION = RADIATION.sort_values(['unix'])
    RADIATION.reset_index(inplace=True)

    SUNRISE = pd.read_csv('sunrise.csv')
    SUNRISE.columns = ['num','unix','date','time','value', 'ex']  
    
    SUNSET = pd.read_csv('sunset.csv')    
    SUNSET.columns = ['num','unix','date','time','value', 'ex']  
    
    TEMPERATURE = pd.read_csv('temperature.csv')
    TEMPERATURE.columns = ['num','unix','date','time','value', 'ex']  
    
    WIND_DIRECTION = pd.read_csv('wind direction in degrees.csv')
    WIND_DIRECTION.columns = ['num','unix','date','time','value', 'ex']   
    
    WIND_SPEED = pd.read_csv('wind speed.csv')
    WIND_SPEED.columns = ['num','unix','date','time','value', 'ex']   

    ENERGY = energy(RADIATION['value'], 72, 0.2)
    AVERAGE_RADIATION = dailyAvg(RADIATION['value'], 276)
    MAX_RADIATION = dailyMax(RADIATION['value'], 276)
      
    
    #Calculated radiation at the atmosphere
    radiation_extraterrestrial = [atmosphere_solarIrradiance(19.602, w, 9*30) for w in range(-180,181)]
    radiation_surface = [surface_solarIrradiance('tropical', 0, 19.602, w, 9*30, 2.5) for w, Gon in zip(range(-180, 180),radiation_extraterrestrial)]
    radiation_extraterrestrial  = [0 if i < 0 else i for i in radiation_extraterrestrial]
    radiation_surface  = [0 if i < 0 else i for i in radiation_surface]

    #plt.plot(radiation_extraterrestrial, 'go')   
    plt.plot(radiation_surface, 'yo')   
    
    val1 = max(radiation_extraterrestrial)
    val2 = RADIATION['value'][0:277].max()
    print(1 - val2/val1)
    
    day=1
    RADIATION['hour angle'] = unix2hourangle(RADIATION['unix'][0+(day-1)*276:276*day].min(), RADIATION['unix'][0+(day-1)*276:276*day])
    #plt.plot(RADIATION['hour angle'][0+(day-1)*276:276*day], RADIATION['value'][0+(day-1)*276:276*day], 'ro')   
    plt.xlabel('Hour Angle (deg)', fontsize=18)
    plt.ylabel('Radiation (Watts/m^2)', fontsize=18)
    plt.title('Earth Radiation', fontsize=20)
    
    
#    df =pd.DataFrame()
#    df = add('test',41.2, 1, 3, df)
#    make_plot(df)
#
#
#    power0 = [panelrad(i, 0, 19.602, 9*30) for i in radiation_surface]
#    power20 = [panelrad(i, 20, 19.602, 9*30) for i in radiation_surface]
#    power45 = [panelrad(i, 45, 19.602, 9*30) for i in radiation_surface]
##    power60 = [panelrad(i, 60, 19.602, 9*30) for i in radiation_surface]
#
#    p1=plt.plot(power0, linewidth =3)
#    p2=plt.plot(power20, linewidth =3)
#    p3=plt.plot(power45, linewidth =3)
##    p4=plt.plot(power45)
#    plt.title('Power over Beta Angle', fontsize=20)
#    plt.xlabel('Hour Angle (deg)', fontsize=18)
#    plt.ylabel('Power (Watts)', fontsize=18)
#    plt.legend(["Beta = 0" , "Beta = 20", "Beta = 45", "Beta = 60"])
