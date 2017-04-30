#!/usr/bin/python
#
# Utilities to manipulate time and date values
#

def roundTime(time):
  timeOut = time[0:2] + time[3:5]
  if int(time[6:7]) >= 30:
    timeOut = int(timeOut)+1
  return timeOut

def toDecHours(time):
  if len(time) == 3:
    timeOut = float(int(time[0:1])) + float(int(time[1:3]))/60.0
  elif len(time) == 4:
    timeOut = float(int(time[0:2])) + float(int(time[2:4]))/60.0
  else:
    timeOut = float(int(time[0:2])) + float(int(time[3:5]))/60.0 + float(int(time[6:8]))/3600.0
  return timeOut

def isLeap(date):
  year = int(date[0:4])
  if (year%4 != 0 or (year%100 == 0 and year%400 != 0)):
    return 0
  else:
    return 1

def dayInYear(dayIn,leap):
  month = int(dayIn[5:7])
  day = int(dayIn[8:10])
  dayOut = 0
  daysInMonth = []
  if leap == 1:
    daysToMonth = [31,29,31,30,31,30,31,31,30,31,30,31]
  else:
    daysToMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
  for monthIndex in range(0,month-1):
    dayOut = dayOut + daysToMonth[monthIndex]
  dayOut = dayOut + day
  return dayOut

