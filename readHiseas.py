#!/usr/bin/python
#
# Reads all Hiseas data
#

import sys
import readData
import reorder
import vectorize
import timeManipulation as tm

def read(dir):
  if dir != "" and dir[len(dir)-1:len(dir)] != "/":
    dir = dir + "/"
  ending = ""
  
  solarradiationFile = dir + "solarradiation" + ending + ".csv"
  humidityFile = dir + "humidity" + ending + ".csv"
  pressureFile = dir + "barometricpressure" + ending + ".csv"
  temperatureFile = dir + "temperature" + ending + ".csv"
  windspeedFile = dir + "windspeed" + ending + ".csv"
  winddirectionFile = dir + "winddirectionindegrees" + ending + ".csv"
  sunriseFile = dir + "sunrise.csv"
  sunsetFile = dir + "sunset.csv"
  
  solarradiationData = readData.read(solarradiationFile)
  humidityData = readData.read(humidityFile)
  pressureData = readData.read(pressureFile)
  temperatureData = readData.read(temperatureFile)
  windspeedData = readData.read(windspeedFile)
  winddirectionData = readData.read(winddirectionFile)
  sunriseData = readData.read(sunriseFile)
  sunsetData = readData.read(sunsetFile)
  
  dataSize = len(solarradiationData)-1
  sunupSize = len(sunriseData)-1

  midday = []
  for dataIndex in range(0,sunupSize):
    sunrise = float(tm.toDecHours(sunriseData[dataIndex][4]))
    sunset = float(tm.toDecHours(sunsetData[dataIndex][4]))
    midday.append((sunrise + sunset)/2.0)
  
  ctr = 0
  day = []
  dayOfYear = []
  sunup = []
  previousTime = tm.roundTime(solarradiationData[0][3])
  for dataIndex in range(0,dataSize):
    if int(previousTime) < int(tm.roundTime(solarradiationData[dataIndex][3])) and ctr < sunupSize-1:
      ctr = ctr+1
    if int(tm.roundTime(solarradiationData[dataIndex][3])) >= int(sunriseData[ctr][4]) and \
       int(tm.roundTime(solarradiationData[dataIndex][3])) <= int(sunsetData[ctr][4]):
      sunup.append(1)
    else:
      sunup.append(0)
    previousTime = tm.roundTime(solarradiationData[dataIndex][3])
    day.append(ctr+1)
    dayOfYear.append(tm.dayInYear(solarradiationData[dataIndex][2],1))
  
  combinedData = []
  for dataIndex in range(0,dataSize):
    dataRow = [dayOfYear[dataIndex],solarradiationData[dataIndex][0],solarradiationData[dataIndex][1],
               solarradiationData[dataIndex][2],solarradiationData[dataIndex][3],solarradiationData[dataIndex][4],
               humidityData[dataIndex][4],pressureData[dataIndex][4],temperatureData[dataIndex][4],windspeedData[dataIndex][4],
               winddirectionData[dataIndex][4],sunup[dataIndex]]
    combinedData.append(dataRow)
  
  header = ["day","index","unixTime","date","time","radiation","humidity","pressure","temperature","windSpeed","windDirn",
            "sunUp"]
  
  combinedData = reorder.ascending(combinedData)
  #readData.writeSpaced( "HiseasDataTabbed.dat",header,combinedData )

  return combinedData, midday

def variableIndex( varName ):
  if varName == "day":
    return 0
  elif varName == "index":
    return 1
  elif varName == "unixtime":
    return 2
  elif varName == "date":
    return 3
  elif varName == "time":
    return 4
  elif varName == "radiation":
    return 5
  elif varName == "humidity":
    return 6
  elif varName == "pressure":
    return 7
  elif varName == "temperature":
    return 8
  elif varName == "windspeed":
    return 9
  elif varName == "winddirn":
    return 10
  elif varName == "sunup":
    return 11




