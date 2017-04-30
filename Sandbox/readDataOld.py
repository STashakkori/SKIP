#!/usr/bin/python
#
# This script reads the csv data
#

def read( inputFile ):
  allData=[]
  with open(inputFile,'r') as csvfile:
    for line in csvfile:
      #values = line.split()
      allData.append([value for value in line.split()])
  return allData

#Standalone which only columnizes the data without averaging
if __name__ == '__main__':
  import sys

  inputFile = str(sys.argv[1])
  #outputFile = str(sys.argv[2])
  data = read(inputFile)
  print data[0]
  #write(outputFile)

