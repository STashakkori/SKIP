#!/usr/bin/python
#
# Computes the normalized radiation deviation value
#

def linear(temp,press,humid,speed,dirn,params):
  value = (float(params[0]) + float(params[1])*float(temp) + float(params[2])*float(press) + float(params[3])*float(humid) \
          + float(params[4])*float(speed) + float(params[5])*float(dirn))
  return value

def quadratic(temp,press,humid,speed,dirn,params):
  value = (float(params[0]) + float(params[1])*float(temp) + float(params[2])*float(press) + float(params[3])*float(humid) \
          + float(params[4])*float(speed) + float(params[5])*float(dirn) \
          + float(params[6])*float(temp)*float(temp) + float(params[7])*float(temp)*float(press) + float(params[8])*float(temp)*float(humid) \
          + float(params[9])*float(temp)*float(speed) + float(params[10])*float(temp)*float(dirn) \
          + float(params[11])*float(press)*float(press) + float(params[12])*float(press)*float(humid) + float(params[13])*float(press)*float(speed) \
          + float(params[14])*float(press)*float(dirn) \
          + float(params[15])*float(humid)*float(humid) + float(params[16])*float(humid)*float(speed) + float(params[17])*float(humid)*float(dirn) \
          + float(params[18])*float(speed)*float(speed) + float(params[19])*float(speed)*float(dirn) \
          + float(params[20])*float(dirn)*float(dirn))
  return value

