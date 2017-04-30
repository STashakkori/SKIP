#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 09:10:02 2017

@author: tammystatham
"""

import numpy as np
import marstime
import matplotlib.pyplot as plt
import datetime

def ls_calculator(jd):
    ls = marstime.Mars_Ls(jd)
    return ls

def declination_mars(j2000_offsets):   
    ''' Calculates the declination based on the time of the day that it is. 
        INPUT: jd is the julian day'''
        
    dec = marstime.solar_declination(marstime.Mars_Ls(j2000_offsets)) #takes Ls, not MSD
    
    return dec

def atmosphere_solarIrradiance_mars(jd, lat, dec):
    '''INPUT: n is the number of the day in the year
              w is the solar hour
              lat is the latitude that you are currently at'''
    
    e = 0.0934
    lsp = np.deg2rad(248)   
    Gsc = 590 #W/m^2
    ls = np.deg2rad(ls_calculator(jd))
    
    lat = np.deg2rad(lat)
    dec= np.deg2rad(dec)
    
    rbar_over_r = (1+e*np.cos(ls - lsp))/(1-e**2)
#    x = marstime.subsolar_longitude(jd)
    h = marstime.hourangle(0, jd)
    cosz = np.sin(lat)*np.sin(dec) + np.cos(lat)*np.cos(dec)*np.cos(h)
#    z = np.deg2rad(marstime.solar_zenith(x,0,jd))
    S = Gsc*cosz*(rbar_over_r**2)

    return(S)

def greg2julian (YEAR,MONTH,DAY):
#
#---COMPUTES THE JULIAN DATE (JD) GIVEN A GREGORIAN CALENDAR
#   DATE (YEAR,MONTH,DAY).

    I= YEAR
    J= MONTH
    K= DAY

    JD= K-32075+1461*(I+4800+(J-14)/12)/4+367*(J-2-(J-14)/12*12) /12-3*((I+4900+(J-14)/12)/100)/4

    return JD

def day2date(n):
    dt = datetime.datetime(2017,1,1)
    dtdelta = datetime.timedelta(days=n)
    
    return(dt + dtdelta)

if __name__ == '__main__':
    
    jd = 200 #offset from  Jan 1, 2000 - starting Julian Date
    lat = 0
    start_j2000_ott = 151.27365

    #create the calendar array with 120 points, adding days to propagate in the future
    msd = np.linspace(0,1,800)

    #calculate the j2000 offset dates
    j2000_offsets = marstime.j2000_from_Mars_Solar_Date(msd + marstime.Mars_Solar_Date(jd))
    
    dec= declination_mars(j2000_offsets) 
    eot = marstime.equation_of_time(j2000_offsets)*60/15. #convert from degrees to minutes
    
    h = marstime.hourangle(0, j2000_offsets)

    S= atmosphere_solarIrradiance_mars(j2000_offsets, lat, dec) 
    S = [0 if i < 0 else i for i in S]

    plt.plot(np.rad2deg(h)+180, S,'ro')
    plt.xlabel('Hour Angle (deg)', fontsize=18)
    plt.ylabel('Radiation (Watts/m^2)', fontsize=18)
    plt.title('Mars Radiation', fontsize=20)
