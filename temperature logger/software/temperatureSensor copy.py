import os
import glob
import time
from datetime import datetime
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
 

device_file = "." + '/temps.txt'
date_format = '%d %H:%M:%S'
 
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
        print ("line",l)
        tempPos = l.find('temperature=')
        print ("tempPos",tempPos)
        timePos = l.find('at ')
        print ("timePos",timePos)
        if tempPos != -1 and  timePos!=-1:
            temp=re.findall('temperature=(.+?) at', l)
            print ("temp",temp)
            ti=re.findall('at (.*)', l)
            tim= "".join(str(element) for element in ti)
            #print ("tim",tim)
            date_obj = datetime.strptime(tim, date_format)
            print ("time",date_obj)
            yVals.append(temp)
            xVals.append(date_obj)
    return xVals, yVals



    #text='Temperature='+str(read_temp()) + ' \tat \t' +datetime.datetime.now().strftime('%d %H:%M:%S')+ '\t'+str(time.time())
xVals, yVals=readTempAndTime()
# x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
# y = [i for i,_ in enumerate(x)]

# plot
plt.plot([],[])
plt.scatter(xVals,yVals)

# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter(date_format)
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
plt.close()
