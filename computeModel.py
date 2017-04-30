#!/usr/bin/python
#
# Attempts to correlate the data
#
import sys
import readData
import reorder
import vectorize
import readHiseas
import timeManipulation as tm
import numpy as np
import solarData
import powerModel
import parameters
import computeNormRad

def computeModel(normDev,temperature,pressure,humidity,windspeed,winddirn,pwrModel):
  dataSize = len(normDev)
  humidityCoeff = 1.0
  modeledNormRad = []
  SSres = 0.0
  SSreg = 0.0
  SStot = 0.0
  avgNormDev = sum(normDev)/float(len(normDev))
  paramsOut = []
  
  if pwrModel == "linear" or pwrModel == "lin":
    params = powerModel.modelParamsLin(normDev,temperature,pressure,humidity,windspeed,winddirn,humidityCoeff)
    for index in range(0,6):
      paramsOut.append(params[0,index])
    for dataIndex in range(0,len(normDev)):
      value = computeNormRad.linear(float(temperature[dataIndex])+459.67,float(pressure[dataIndex]),float(humidity[dataIndex])/100.0,float(windspeed[dataIndex]),float(winddirn[dataIndex]),paramsOut)
      modeledNormRad.append(value)
      SSres = SSres + (normDev[dataIndex] - value)**2.0
      SSreg = SSreg + (avgNormDev - value)**2.0
      SStot = SStot + (normDev[dataIndex] - avgNormDev)**2.0
  elif pwrModel == "quadratic" or pwrModel == "quad":
    params = powerModel.modelParamsQuad(normDev,temperature,pressure,humidity,windspeed,winddirn,humidityCoeff)
    for index in range(0,21):
      paramsOut.append(params[0,index])
    for dataIndex in range(0,len(normDev)):
      value = computeNormRad.quadratic(float(temperature[dataIndex])+459.67,float(pressure[dataIndex]),float(humidity[dataIndex])/100.0,float(windspeed[dataIndex]),float(winddirn[dataIndex]),paramsOut)
      modeledNormRad.append(value)
      SSres = SSres + (normDev[dataIndex] - value)**2.0
      SSreg = SSreg + (avgNormDev - value)**2.0
      SStot = SStot + (normDev[dataIndex] - avgNormDev)**2.0
  else:
    print("ERROR: Incorrect power model selection.")

  print("Data fit R^2 values:")
  print "  R^2  = " + str(1.0-SSres/SStot)
  print "  R^2 ?= " + str(SSreg/SStot)

  modeledRad = []
  for dataIndex in range(0,len(modeledNormRad)):
    modeledRad.append(float(nominalRadOrderedSunny[dataIndex]) * (1.0 - float(modeledNormRad[dataIndex])))
  
  orderedModeled = []
  orderedModeled.append(indicesOrderedSunny)
  orderedModeled.append(modeledNormRad)
  orderedModeled.append(normDev)
  orderedModeled.append(modeledRad)
  orderedModeled.append(radiationOrderedSunny)
  header = ["index","modelNormRad","normRad","modelRad","rad"]
  readData.writeSpaced("testModeled.dat",header,zip(*orderedModeled))

  return paramsOut

if __name__ == '__main__':
  direc = sys.argv[1]
  pwrModel = sys.argv[2]
  
  combinedData,midday = readHiseas.read(direc)
  
  # Indices for various data values
  dayIndex = readHiseas.variableIndex("day")
  indexIndex = readHiseas.variableIndex("index")
  unixtimeIndex = readHiseas.variableIndex("unixtime")
  dateIndex = readHiseas.variableIndex("date")
  timeIndex = readHiseas.variableIndex("time")
  radiationIndex = readHiseas.variableIndex("radiation")
  humidityIndex = readHiseas.variableIndex("humidity")
  pressureIndex = readHiseas.variableIndex("pressure")
  temperatureIndex = readHiseas.variableIndex("temperature")
  windspeedIndex = readHiseas.variableIndex("windspeed")
  winddirnIndex = readHiseas.variableIndex("winddirn")
  sunupIndex = readHiseas.variableIndex("sunup")
  
  # Order data by the day of the year
  daylistOrdered = vectorize.returnAVector(combinedData,dayIndex)
  datelistOrdered = vectorize.returnAVector(combinedData,dateIndex)
  timeOrdered = vectorize.returnAVector(combinedData,timeIndex)
  radiationOrdered = vectorize.returnAVector(combinedData,radiationIndex)
  humidityOrdered = vectorize.returnAVector(combinedData,humidityIndex)
  pressureOrdered = vectorize.returnAVector(combinedData,pressureIndex)
  temperatureOrdered = vectorize.returnAVector(combinedData,temperatureIndex)
  windspeedOrdered = vectorize.returnAVector(combinedData,windspeedIndex)
  winddirnOrdered = vectorize.returnAVector(combinedData,winddirnIndex)
  sunupOrdered = vectorize.returnAVector(combinedData,sunupIndex)
  
  firstDay = daylistOrdered[0]
  
  # Compute deviation between nominal radiation and Hiseas radiation, and then normalize it
  nominalRadOrdered = []
  deviationOrdered = []
  normalizedDeviationOrdered = []
  indicesOrdered = []
  for dataIndex in range(0,len(daylistOrdered)):
    leap = tm.isLeap(datelistOrdered[dataIndex])
    day = daylistOrdered[dataIndex]
    hour = tm.toDecHours(timeOrdered[dataIndex])
    nominalRad = solarData.nominalRadiation(day,hour,midday[day-firstDay],leap)
    nominalRadOrdered.append(nominalRad)
    deviation = max(0.0,nominalRad - float(radiationOrdered[dataIndex]))
    deviationOrdered.append(deviation)
    #normalizedDeviation = float(deviation)/max(float(nominalRad),1.0e-6)
    normalizedDeviation = float(deviation)/max(float(nominalRad),float(radiationOrdered[dataIndex]))
    normalizedDeviationOrdered.append(normalizedDeviation)
    indicesOrdered.append(dataIndex)
  
  # Cull data from before sunrise and after sunset
  indicesOrderedSunny = vectorize.daylightVector(sunupOrdered,indicesOrdered)
  daylistOrderedSunny = vectorize.daylightVector(sunupOrdered,daylistOrdered)
  timeOrderedSunny = vectorize.daylightVector(sunupOrdered,timeOrdered)
  radiationOrderedSunny = vectorize.daylightVector(sunupOrdered,radiationOrdered)
  humidityOrderedSunny = vectorize.daylightVector(sunupOrdered,humidityOrdered)
  pressureOrderedSunny = vectorize.daylightVector(sunupOrdered,pressureOrdered)
  temperatureOrderedSunny = vectorize.daylightVector(sunupOrdered,temperatureOrdered)
  windspeedOrderedSunny = vectorize.daylightVector(sunupOrdered,windspeedOrdered)
  winddirnOrderedSunny = vectorize.daylightVector(sunupOrdered,winddirnOrdered)
  nominalRadOrderedSunny = vectorize.daylightVector(sunupOrdered,nominalRadOrdered)
  deviationOrderedSunny = vectorize.daylightVector(sunupOrdered,deviationOrdered)
  normalizedDeviationOrderedSunny = vectorize.daylightVector(sunupOrdered,normalizedDeviationOrdered)
  
#  # Inspect for a single day
#  day = dayInput
#  
#  indicesOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,indicesOrderedSunny,day)
#  radiationOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,radiationOrderedSunny,day)
#  humidityOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,humidityOrderedSunny,day)
#  pressureOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,pressureOrderedSunny,day)
#  temperatureOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,temperatureOrderedSunny,day)
#  windspeedOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,windspeedOrderedSunny,day)
#  winddirnOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,winddirnOrderedSunny,day)
#  nominalRadOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,nominalRadOrderedSunny,day)
#  deviationOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,deviationOrderedSunny,day)
#  normalizedDeviationOrderedSunnyOneday = vectorize.returnADay(daylistOrderedSunny,normalizedDeviationOrderedSunny,day)
#  orderedSunnyOneday = []
#  orderedSunnyOneday.append(indicesOrderedSunnyOneday)
#  orderedSunnyOneday.append(radiationOrderedSunnyOneday)
#  orderedSunnyOneday.append(nominalRadOrderedSunnyOneday)
#  orderedSunnyOneday.append(deviationOrderedSunnyOneday)
#  orderedSunnyOneday.append(normalizedDeviationOrderedSunnyOneday)
#  #orderedSunnyOneday.append(humidityOrderedSunnyOneday)
#  
#  #headerOrderedSunnyOneday = ["radiation","humidity"]
#  headerOrderedSunnyOneday = ["index","radiation","nominal","deviation","normDev"]
#  readData.writeSpaced("testOrderedSunnyOneday.dat",headerOrderedSunnyOneday,zip(*orderedSunnyOneday))
  
  #output = "Humidity:    " + str(np.corrcoef(radiationOrderedSunny,humidityOrderedSunny)[0,1])
  #print(output)
  #output = "Pressure:    " + str(np.corrcoef(radiationOrderedSunny,pressureOrderedSunny)[0,1])
  #print(output)
  #output = "Temperature: " + str(np.corrcoef(radiationOrderedSunny,temperatureOrderedSunny)[0,1])
  #print(output)
  #output = "Wind speed:  " + str(np.corrcoef(radiationOrderedSunny,windspeedOrderedSunny)[0,1])
  #print(output)
  #output = "Wind direct: " + str(np.corrcoef(radiationOrderedSunny,winddirnOrderedSunny)[0,1])
  #print(output)
  
  orderedSunny = []
  orderedSunny.append(indicesOrderedSunny)
  orderedSunny.append(radiationOrderedSunny)
  orderedSunny.append(nominalRadOrderedSunny)
  orderedSunny.append(deviationOrderedSunny)
  orderedSunny.append(normalizedDeviationOrderedSunny)
  headerOrderedSunny = ["index","radiation","nominal","deviation","normDev"]
  readData.writeSpaced("testOrderedSunny.dat",headerOrderedSunny,zip(*orderedSunny))

  print("Correlation coefficients with weather data:")
  output = "  Humidity:    " + str(np.corrcoef(normalizedDeviationOrderedSunny,humidityOrderedSunny)[0,1])
  print(output)
  output = "  Pressure:    " + str(np.corrcoef(normalizedDeviationOrderedSunny,pressureOrderedSunny)[0,1])
  print(output)
  output = "  Temperature: " + str(np.corrcoef(normalizedDeviationOrderedSunny,temperatureOrderedSunny)[0,1])
  print(output)
  output = "  Wind speed:  " + str(np.corrcoef(normalizedDeviationOrderedSunny,windspeedOrderedSunny)[0,1])
  print(output)
  output = "  Wind direct: " + str(np.corrcoef(normalizedDeviationOrderedSunny,winddirnOrderedSunny)[0,1])
  print(output)
  
  pwrModel = "quadratic"
  #params = computeModel(normalizedDeviationOrderedSunny,temperatureOrderedSunny,pressureOrderedSunny,humidityOrderedSunny,windspeedOrderedSunny,winddirnOrderedSunny,"linear")
  params = computeModel(normalizedDeviationOrderedSunny,temperatureOrderedSunny,pressureOrderedSunny,humidityOrderedSunny,windspeedOrderedSunny,winddirnOrderedSunny,"quadratic")

  paramFile = "params.dat"
  parameters.write(paramFile,pwrModel,params)
#  testModel,testParams = parameters.read(paramFile)




