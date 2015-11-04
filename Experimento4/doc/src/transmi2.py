#!/usr/bin/python


import serial
import datetime
import time 
import matplotlib.pyplot as plt
import csv

size = 500
arrtension = [size]
arrtiempo = [size]
startime = time.time()
ser = serial.Serial('/dev/cu.usbmodem1411',115200)  #60A78A81  open serial port

log_file = open("["+datetime.datetime.now().ctime() + "data " +".csv", "wb")
writer   = csv.writer(log_file, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)


for x in range (0, size):
    tiempo = time.time()-startime
    tension = ser.readline()
    arrtension.append(tension)
    arrtiempo.append(tiempo)
    writer.writerow(str(arrtiempo[x])+str(arrtension[x]))


ser.close()
tension_flotante = map(float, arrtension)

plt.plot(arrtiempo,arrtension, 'ro')
plt.ylim([-5,5])
plt.xlim([0,0.1])
plt.ylabel('Tension en Volt')
plt.xlabel('Tiempo')
plt.show()
