import os
import glob
import time
import random
from datetime import datetime
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 

device_file = ".." + '/results/runLog.txt'
#device_file = ".." + '/results/runLogShort.txt'
date_format = '%d %H:%M:%S'
DEBUG=False
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


 
def readTempAndTime():
    lines = read_temp_raw()
    xVals=[]
    yVals=[]
    for l in lines:
        if DEBUG: print ("line:",l)
        tempPos = l.find('Temperature=')
        if DEBUG: print ("tempPos",tempPos)
        timePos = l.find('\tat')
        if DEBUG: print ("timePos",timePos)
        if tempPos != -1 and  timePos!=-1:
            temp=re.findall('Temperature=(.+?)\tat', l)
            if DEBUG: print ("temp",temp)
            ti=re.findall('at \t(.*)\t', l)
            tim= "".join(str(element) for element in ti)
            if DEBUG: print ("tim",tim)
            date_obj = datetime.strptime(tim, date_format)
            if DEBUG: print ("time",date_obj)
            yVals.append(temp)
            xVals.append(date_obj)
    return xVals, yVals



    #text='Temperature='+str(read_temp()) + ' \tat \t' +datetime.datetime.now().strftime('%d %H:%M:%S')+ '\t'+str(time.time())
xVals, yVals=readTempAndTime()
# x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
# y = [i for i,_ in enumerate(x)]

# plot
plt.plot([],[])
plt.plot([1,2,3,5,6], [1, 2, 3, 4, 6])
#plt.plot(xVals,yVals)

# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter(date_format)
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
plt.close()

# x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
# y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

# # plot
# plt.plot([],[])
# plt.scatter(x,y)

# # beautify the x-labels
# plt.gcf().autofmt_xdate()
# myFmt = mdates.DateFormatter('%H:%M')
# plt.gca().xaxis.set_major_formatter(myFmt)

# plt.show()
# plt.close()