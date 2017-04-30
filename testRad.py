#!/usr/bin/python

import radiationCurve

temp = [56.0,58.0,60.0]
press = [30.43,30.43,30.43]
humid = [60,71,99]
speed = [7.87,15.0,25.0]
dirn = [21.43,0.0,170.0]
sunup = "613"
sundn = "1812"
date = "2016-09-30"
time = "15:30:32"

rad = radiationCurve.compute(temp,press,humid,speed,dirn,sunup,sundn,date,time,"params.dat")

print(rad)



