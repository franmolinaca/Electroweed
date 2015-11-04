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

#Ejes del grafico de matplotlib
plt.axis([0, 100, -1, 6])
#Plot en modo interactivo
plt.ion()
#Mostrar el grafico
plt.show()

#Ciclo de muestreo 
for x in range (0, size):

	#Tome el tiempo del momento
    tiempo = time.time()-startime
    #Tome la tensión del momento
    tension = ser.readline()
    #Imprima para pruebas
    print tension
    print tiempo
    #Escriba en el log
    writer.writerow(str(tiempo)+str(tension))
    #Adjunte al gráfico plt
    plt.scatter(tiempo, tension)
    plt.draw()
    #Espere un tiempo para tomar otro dato
    time.sleep(0.001)

#Cierre el puerto
ser.close()

