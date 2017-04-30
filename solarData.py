#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:54:08 2017

@author: tammystatham
"""

#import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
#import os

def energy(rad, area, efficiency):
    '''rad is the radiation on the earth's surface
       area is the m'2 area of the solar panel
       efficency of the solar panel'''

    e = rad*area*efficiency
    return e

def panelrad(rad, beta, lat, dec):
    prad = (rad*np.sin(90 - lat + dec+beta))/np.sin(90 - lat + dec)
    
    return prad

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

def solarHour(hour,midday=None):
    '''INPUT: hour is the decimal number hour in the day '''
    
    if midday is None:
        w = 15*(hour - 12)
    else:
        w = 15*(hour - midday)
    return(w)

def atmosphere_solarIrradiance(lat, w, n, leap=None):
    '''INPUT: n is the number of the day in the year
              w is the solar hour
              lat is the latitude that you are currently at'''
    
    w = np.deg2rad(w) #solar hour
    lat = np.deg2rad(lat) #latitude
    
    dec = declination(n,leap)
    
    Gsc = 1367 #W/m^2
    Gon = Gsc*(1+0.033*np.cos(2*np.pi*n/365))
    Go = Gon*(np.cos(lat)*np.cos(dec)*np.cos(w)+np.sin(lat)*np.sin(dec))
    
    return(Go)

def unix2hourangle(unix1, unix2):
    ''' Given 2 unix times, this calculates the sidereal time
        Unix 1 is the begnning of the day
        Unix 2 is the current time'''
    
    seconds = unix2 - unix1
    hour = seconds/3600
    w = solarHour(hour) + 180
    
    return(w)

def declination(n,leap=None):   
    ''' Calculates the declination based on the time of the day that it is. '''
    if leap is None:
      dec = np.deg2rad(23.45) * np.sin(2*np.pi*(284 + n)/365) #dec
    elif leap == 1:
      dec = np.deg2rad(23.45) * np.sin(2*np.pi*(284 + n)/366) #dec
    else:
      dec = np.deg2rad(23.45) * np.sin(2*np.pi*(284 + n)/365) #dec
    return dec
    
def surface_solarIrradiance(climate_type, thetaz, lat, w, n, A, leap=None):
    """INPUT: climate_type is the region and season for the area
              n is the number of the day in the year (deg)
              w is the solar hour (deg)
              lat is the latitude that you are currently at (deg)
              thetaz is the solar incidence angle off of nadir (deg)"""
    Gsc = 1367 #W/m^2

    w = np.deg2rad(w)
    lat = np.deg2rad(lat)
    dec = declination(n,leap)
    
    thetaz = np.deg2rad(thetaz)
    
    if climate_type == 'tropical':
        r0 = 0.95
        r1 = 0.98
        rk = 1.02
    elif climate_type == 'midlatitude_summer':
        r0 = 0.97
        r1 = 0.99
        rk = 1.02        
    elif climate_type == 'subarctic_summer':
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
#    Gcb = tb*Gon*(np.cos(lat)*np.cos(dec)*np.cos(w) + np.sin(lat)*np.sin(dec))
    
    td = 0.271 - 0.294*tb
#    Gcd = td * Gon * (np.cos(lat)*np.cos(dec)*np.cos(w) + np.sin(lat)*np.sin(dec))
    
    Gc = (tb + td)*Gsc*(1+0.033*np.cos(2*np.pi*n/365))*(np.cos(lat)*np.cos(dec)*np.cos(w) + np.sin(lat)*np.sin(dec))
#    Gc = Gcb + Gcd
    return(Gc)

def nominalRadiation( day, hour=None, midday=None, radType="surf", leap=None ):
    #Calculated radiation at the atmosphere
    if hour is None and midday is None:
        radiation_extraterrestrial = [atmosphere_solarIrradiance(19.602, w, day, leap) for w in range(-180,181)]
        radiation_surface = [surface_solarIrradiance('tropical', 0, 19.602, w, day, 2.5, leap) for w, Gon in zip(range(-180, 180),radiation_extraterrestrial)]
        radiation_extraterrestrial  = [0 if i < 0 else i for i in radiation_extraterrestrial]
        radiation_surface = [0 if i < 0 else i for i in radiation_surface]
    else:
        w = solarHour( hour,midday )
        radiation_extraterrestrial = max(atmosphere_solarIrradiance(19.602, w, day, leap),0.0)
        radiation_surface = max(surface_solarIrradiance('tropical', 0, 19.602, w, day, 2.5, leap),0.0)
    if radType == "ext":
      return radiation_extraterrestrial
    else:
      return radiation_surface

#if __name__ == '__main__':
#        
#    os.chdir('Space Apps data')
#   
#    PRESSURE = pd.read_csv('barometric pressure.csv', header=None)
#    PRESSURE.columns = ['num','unix','date','time','value', 'ex']
#    
#    HUMIDITY = pd.read_csv('humidity.csv', header=None)
#    HUMIDITY.columns = ['num','unix','date','time','value', 'ex']
#
#    RADIATION = pd.read_csv('solar radiation.csv') 
#    RADIATION.columns = ['num','unix','date','time','value', 'ex']
#    RADIATION = RADIATION.sort_values(['unix'])
#    RADIATION.reset_index(inplace=True)
#
#    SUNRISE = pd.read_csv('sunrise.csv')
#    SUNRISE.columns = ['num','unix','date','time','value', 'ex']  
#    
#    SUNSET = pd.read_csv('sunset.csv')    
#    SUNSET.columns = ['num','unix','date','time','value', 'ex']  
#    
#    TEMPERATURE = pd.read_csv('temperature.csv')
#    TEMPERATURE.columns = ['num','unix','date','time','value', 'ex']  
#    
#    WIND_DIRECTION = pd.read_csv('wind direction in degrees.csv')
#    WIND_DIRECTION.columns = ['num','unix','date','time','value', 'ex']   
#    
#    WIND_SPEED = pd.read_csv('wind speed.csv')
#    WIND_SPEED.columns = ['num','unix','date','time','value', 'ex']   
#
#    ENERGY = energy(RADIATION['value'], 72, 0.2)
#    AVERAGE_RADIATION = dailyAvg(RADIATION['value'], 276)
#    MAX_RADIATION = dailyMax(RADIATION['value'], 276)
#      
#    
##    plt.plot((RADIATION['unix']-RADIATION['unix'].min())/3600/24, RADIATION['value'])    
##    plt.plot(AVERAGE_RADIATION, 'ro')
##    plt.plot(MAX_RADIATION, 'go')   
#    
#    #Calculated radiation at the atmosphere
#    radiation_extraterrestrial = [atmosphere_solarIrradiance(19.602, w, 9*30) for w in range(-180,181)]
#    radiation_surface = [surface_solarIrradiance('tropical', 0, 19.602, w, 9*30, 2.5) for w, Gon in zip(range(-180, 180),radiation_extraterrestrial)]
#    radiation_extraterrestrial  = [0 if i < 0 else i for i in radiation_extraterrestrial]
#    radiation_surface = [0 if i < 0 else i for i in radiation_surface]
#
#    
#    plt.plot(radiation_extraterrestrial, 'go')   
#    plt.plot(radiation_surface, 'yo')   
#    
#    
#    val1 = max(radiation_extraterrestrial)
#    val2 = RADIATION['value'][0:277].max()
#    print(1 - val2/val1)
#    
#    day=1
#    RADIATION['hour angle'] = unix2hourangle(RADIATION['unix'][0+(day-1)*276:276*day].min(), RADIATION['unix'][0+(day-1)*276:276*day])
#    plt.plot(RADIATION['hour angle'][0+(day-1)*276:276*day], RADIATION['value'][0+(day-1)*276:276*day], 'ro')   
    


    
