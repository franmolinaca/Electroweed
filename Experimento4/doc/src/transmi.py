#!/usr/bin/python


import serial
import datetime
import time 
import matplotlib.pyplot as plt
import csv

size = 300
arrtension = [size]
arrtiempo = [size]
startime = time.time()
ser = serial.Serial('/dev/cu.usbmodem1411',115200)  #60A78A81  open serial port

log_file = open("["+datetime.datetime.now().ctime() + "data " +".csv", "wb")
writer   = csv.writer(log_file, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

plt.axis([0, 100, -1, 6])
plt.ion()
plt.show()

for x in range (0, size):
    tiempo = time.time()-startime
    tension = ser.readline()
    print tension
    print tiempo
#    arrtension.append(tension)
#    arrtiempo.append(tiempo)
    writer.writerow(str(tiempo)+str(tension))
    plt.scatter(tiempo, tension)
    plt.draw()
    time.sleep(0.001)


ser.close()

#tension_flotante = map(float, arrtension)
#plt.plot(arrtiempo,arrtension, 'ro')
#plt.ylim([-5,5])
#plt.xlim([0,0.1])
#plt.ylabel('Tension en Volt')
#plt.xlabel('Tiempo')
#plt.show()
