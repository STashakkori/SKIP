#!/usr/bin/python
#
# Read/write the model parameters
#

def write(paramFile,pwrModel,params):
  with open(paramFile,'w') as pFile:
    pFile.write(pwrModel + '\n')
    outstring = ""
    for index in range(0,len(params)):
      outstring = outstring + str(params[index]) + '\t'
    outstring = outstring + '\n'
    pFile.write(outstring)

def read(paramFile):
  with open(paramFile,'r') as pFile:
    pwrModel = pFile.readline().strip('\n')
    params = pFile.readline().split()
  return pwrModel,params

