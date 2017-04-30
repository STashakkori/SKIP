#!/usr/bin/bash
#
# Model the solar radiation dependent on the variables
#
#Later, add logic to ignore high humidity times when rad. goes way down

#normalizedModelRad = C_0 + C_T*(temperature+459.67) + C_P*pressure + C_H*humidity + C_Ws*windspeed + C_Wd*winddirn + C_T2*(temperature+459.67)^2
#modelRad = nominalRad*normalizedModelRad

import numpy as np

def modelParamsLin(normalizedRadiation,temperature,pressure,humidity,windspeed,winddirn,humidityCoeff):
  X = []
  normRad = []
  for dataIndex in range(0,len(normalizedRadiation)):
    temp = float(temperature[dataIndex]) + 459.67
    press = float(pressure[dataIndex])
    humid = float(humidity[dataIndex])/100.0
    speed = float(windspeed[dataIndex])
    dirn = float(winddirn[dataIndex])
    X.append([1.0,float(temp),float(press),float(humid),float(speed),float(dirn)])
    normRad.append(float(normalizedRadiation[dataIndex]))
  Xnp = np.matrix(X)
  Xt = np.transpose(Xnp)
  params = np.dot(np.dot(np.linalg.inv(np.dot(Xt,Xnp)),Xt),normRad)

  return params

def modelParamsQuad(normalizedRadiation,temperature,pressure,humidity,windspeed,winddirn,humidityCoeff):
  X = []
  normRad = []
  for dataIndex in range(0,len(normalizedRadiation)):
    temp = float(temperature[dataIndex]) + 459.67
    press = float(pressure[dataIndex])
    humid = float(humidity[dataIndex])/100.0
    speed = float(windspeed[dataIndex])
    dirn = float(winddirn[dataIndex])
    X.append([1.0,float(temp),float(press),float(humid),float(speed),float(dirn), \
              float(temp)*float(temp),float(temp)*float(press),float(temp)*float(humid),float(temp)*float(speed),float(temp)*float(dirn), \
              float(press)*float(press),float(press)*float(humid),float(press)*float(speed),float(press)*float(dirn), \
              float(humid)*float(humid),float(humid)*float(speed),float(humid)*float(dirn), \
              float(speed)*float(speed),float(speed)*float(dirn), \
              float(dirn)*float(dirn)])
    normRad.append(float(normalizedRadiation[dataIndex]))
  Xnp = np.matrix(X)
  Xt = np.transpose(Xnp)
  params = np.dot(np.dot(np.linalg.inv(np.dot(Xt,Xnp)),Xt),normRad)

  return params


