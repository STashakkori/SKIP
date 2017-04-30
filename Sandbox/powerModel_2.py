#!/usr/bin/bash
#
# Model the solar radiation dependent on the variables
#
#Later, add logic to ignore high humidity times when rad. goes way down

#normalizedModelRad = C_0 + C_T*(temperature+459.67) + C_P*pressure + C_H*humidity + C_Ws*windspeed + C_Wd*winddirn + C_T2*(temperature+459.67)^2
#modelRad = nominalRad*normalizedModelRad

import numpy as np

def modelParams(normalizedRadiation,temperature,pressure,humidity,windspeed,winddirn,humidityCutoff):
#def modelParams(normalizedRadiation,temperature,pressure,humidity,humidityCutoff):
#  numParam = 5
#  X = []
#  normRad = []
#  for dataIndex in range(0,len(normalizedRadiation)):
#    # Try an if to avoid when humid > humid_cutoff; then need extra normRad array also omitting values
#    if float(humidity[dataIndex]) < humidityCutoff:
#      temp = float(temperature[dataIndex]) + 459.67
#      X.append([1.0,float(temp),float(pressure[dataIndex]),float(humidity[dataIndex]),float(temp)*float(temp)])
#      normRad.append(float(normalizedRadiation[dataIndex]))
  numParam = 7
  X = []
  normRad = []
  for dataIndex in range(0,len(normalizedRadiation)):
    # Try an if to avoid when humid > humid_cutoff; then need extra normRad array also omitting values
    if float(humidity[dataIndex]) < humidityCutoff:
      temp = float(temperature[dataIndex]) + 459.67
      X.append([1.0,float(temp),float(pressure[dataIndex]),float(humidity[dataIndex]),float(windspeed[dataIndex]),float(winddirn[dataIndex]),float(temp)*float(temp)])
      normRad.append(float(normalizedRadiation[dataIndex]))
  Xnp = np.matrix(X)
  Xt = np.transpose(Xnp)
  params = np.dot(np.dot(np.linalg.inv(np.dot(Xt,Xnp)),Xt),normRad)

  return params


