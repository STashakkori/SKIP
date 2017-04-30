#!/usr/bin/python
#
# This script reads the csv data
#
import csv

def read( inputFile ):
  allData=[]
  with open(inputFile,'rb') as csvFile:
    blah = csv.reader(csvFile,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL)
    for row in blah:
      allData.append(row)
  return allData

#def readDeviation( filename ):

def writeSpaced( outputFile,listHeaders,data ):
  numLists = len(data)
  listSize = len(data[0])
  with open(outputFile,'w') as outFile:
    header = ""
    for listIndex in range(0,listSize):
      header = header + str(listHeaders[listIndex]) + "\t"
    header = header + '\n'
    outFile.write(str(header))
    for dataIndex in range(0,numLists):
      outputString = ""
      for listIndex in range(0,listSize):
        outputString = outputString + str(data[dataIndex][listIndex]) + "\t"
      outputString = outputString + '\n'
      outFile.write(str(outputString))

#Standalone
if __name__ == '__main__':
  import sys

  inputFile = str(sys.argv[1])
  data = read(inputFile)

