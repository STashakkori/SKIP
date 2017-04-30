#!/usr/bin/python
#
# Computes the radiation given the weather inputs, the date, 
#

import parameters
import timeManipulation as tm
import computeNormRad
import solarData

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

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
    for i in np.arange(start_time*2,end_time*2,0.5) :
        df[name][i] = watts

    return(df)    

def delete(name):
    del df[name]

def make_plot(df):
    
    bar_width = 0.45
    opacity = 0.4
    total = df.sum(1,1)-df['time']

    fig = plt.figure()
    
    plt.figure(1)
    plt.bar(df['time'], total, 
            bar_width, 
            alpha=opacity)
    plt.xlabel('Hour in day')
    plt.ylabel('Power (W)')
    plt.title('')
    plt.show()
    
    return(total)

def clear_data():
    
    df =pd.DataFrame()
   

def compute(temperature,pressure,humidity,windspeed,winddirn,sunrise,sunset,date,time,paramFile):
  pwrModel,params = parameters.read(paramFile)
  radiation = []
  for dataIndex in range(0,len(temperature)):
    leap = tm.isLeap(date)
    day = tm.dayInYear(date,leap)
    hour = tm.toDecHours(time)
    midday = (float(tm.toDecHours(sunrise)) + float(tm.toDecHours(sunset)))/2.0
    nominalRad = solarData.nominalRadiation(day,hour,midday,leap)
#    print(leap,day,hour,midday,nominalRad)
    temp = float(temperature[dataIndex])+459.67
    press = float(pressure[dataIndex])
    humid = float(humidity[dataIndex])/100.0
    speed = float(windspeed[dataIndex])
    dirn = float(winddirn[dataIndex])
#    print(temp,press,humid,speed,dirn)
    if pwrModel == "linear":
      model = computeNormRad.linear(temp,press,humid,speed,dirn,params)
    else:
      model = computeNormRad.quadratic(temp,press,humid,speed,dirn,params)
    radiation.append(max(0.0,nominalRad*(1.0 - model)))
  return radiation

if __name__ == '__main__':
    
#    radiation = compute(temperature,pressure,humidity,windspeed,winddirn,sunrise,sunset,date,time,paramFile)
    
    df = add('Lights',100, 17, 22, df)
    make_plot(df,  RADIATION)


