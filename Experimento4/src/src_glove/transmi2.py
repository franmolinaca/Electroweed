#!/usr/bin/python


import serial
import datetime
import time 
import matplotlib.pyplot as plt
import csv

size = 300 #Tamaño de la muestra
arrtension = [size]
arrtiempo = [size]
startime = time.time() #Definir el tiempo inicial

ser = serial.Serial('/dev/cu.usbmodem1411',115200)  #60A78A81  open serial port

#Formato del nombre del archivo log
log_file = open("["+datetime.datetime.now().ctime() + "data " +".csv", "wb") 
#Formato del writer, lo que se escribe al log
writer   = csv.writer(log_file, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

#Ciclo de muestreo 
for x in range (0, size):

	#Tome el tiempo del momento
    tiempo = time.time()-startime
    #Tome la tensión del momento
    tension = ser.readline()
    #Adjunte al arreglo que se pasara a plt
    arrtension.append(tension)
    arrtiempo.append(tiempo)
    #Escriba en el log
    writer.writerow(str(tiempo)+str(tension))

 
#Cierre el puerto
ser.close()

tension_flotante = map(float, arrtension)
#Acomode y grafique
plt.plot(arrtiempo,arrtension, 'ro')
plt.ylim([-5,5])
plt.xlim([0,0.1])
plt.ylabel('Tension en Volt')
plt.xlabel('Tiempo')
plt.show()
