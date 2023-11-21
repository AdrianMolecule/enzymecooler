import os
import glob
import time
import datetime
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def write_temp(newLine):
    f = open('runLog.txt', 'a')
    lines = f.write(newLine)
    f.close()
    return

def initialize_log():
    f = open('runLog.txt', 'w')
    lines = f.write('')
    f.close()
    return
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    
    
initialize_log()
while True:
    text='Temperature='+str(read_temp()) + ' \tat \t' +datetime.datetime.now().strftime('%d %H:%M:%S')+ '\t'+str(time.time())
    write_temp(text+"\n")
    print(text)
    time.sleep(1)