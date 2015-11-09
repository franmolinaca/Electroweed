#!/usr/bin/python


import serial
import datetime
import time 
import matplotlib.pyplot as plt
import csv


vel = raw_input('Defina velocidad deseada')
ang = raw_input('Defina angulo deseado')


ser = serial.Serial('/dev/cu.usbmodem1411',115200)  #60A78A81  open serial port

        
ser.write(vel)
ser.write("\n\r")
ser.write(ang)

#Cierre el puerto
ser.close()