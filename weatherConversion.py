#!/usr/bin/python
#
# Accuweather conversion routines
#

def KtoF(tempK):
  tempF = (float(tempK)-273.15)*1.8 + 32.0
  return tempF

def H2OtoHg(pressH2O):
  pressHg = 0.028959*pressH2O
  return pressHg



