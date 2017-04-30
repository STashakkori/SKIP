#!/usr/bin/python
#
# Reorders the data by the first row of data
#

def ascending( data ):
  dataOut = []
  for index in range(0,366):
    for dataIndex in range(0,len(data)):
      if data[dataIndex][0] == index:
        dataOut.append(data[dataIndex])
  return dataOut



