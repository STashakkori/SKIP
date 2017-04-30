#!/usr/bin/python
#
# Vectorizes the data from columns of the combined data
#

def returnAVector( data,index ):
  vector = []
  dataSize = len(data)
  for dataIndex in range(0,dataSize):
    vector.append(data[dataIndex][index])
  return vector

def daylightVector( sunup,vectorIn ):
  vectorOut = []
  dataSize = len(vectorIn)
  for dataIndex in range(0,dataSize):
    if sunup[dataIndex] == 1:
      vectorOut.append(vectorIn[dataIndex])
  return vectorOut

def returnADay( daylist,vectorIn,day ):
  vectorOut = []
  dataSize = len(vectorIn)
  for dataIndex in range(0,dataSize):
    if int(daylist[dataIndex]) == int(day):
      vectorOut.append(vectorIn[dataIndex])
  return vectorOut




