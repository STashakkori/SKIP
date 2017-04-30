#!/usr/bin/bash
#
# Model the solar radiation dependent on the variables
#
#Later, add logic to ignore high humidity times when rad. goes way down

#normalizedModelRad = C_0 + C_T*(temperature+459.67) + C_P*pressure + C_H*humidity
#modelRad = nominalRad*normalizedModelRad

import numpy as np

def modelParams(normalizedRadiation,temperature,pressure,humidity,windspeed,winddirn,humidityCutoff):
#def modelParams(normalizedRadiation,temperature,pressure,humidity,humidityCutoff):
#  numParam = 4
#  X = []
#  normRad = []
#  for dataIndex in range(0,len(normalizedRadiation)):
#    # Try an if to avoid when humid > humid_cutoff; then need extra normRad array also omitting values
#    if float(humidity[dataIndex]) < humidityCutoff:
#      X.append([1.0,float(temperature[dataIndex])+459.67,float(pressure[dataIndex]),float(humidity[dataIndex])])
#      normRad.append(float(normalizedRadiation[dataIndex]))
  numParam = 6
  X = []
  normRad = []
  for dataIndex in range(0,len(normalizedRadiation)):
    # Try an if to avoid when humid > humid_cutoff; then need extra normRad array also omitting values
    if float(humidity[dataIndex]) < humidityCutoff:
      X.append([1.0,float(temperature[dataIndex])+459.67,float(pressure[dataIndex]),float(humidity[dataIndex]),float(windspeed[dataIndex]),float(winddirn[dataIndex])])
      normRad.append(float(normalizedRadiation[dataIndex]))
  Xnp = np.matrix(X)
  Xt = np.transpose(Xnp)
  params = np.dot(np.dot(np.linalg.inv(np.dot(Xt,Xnp)),Xt),normRad)

  return params


