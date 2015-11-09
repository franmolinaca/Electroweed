#!/usr/bin/python


import serial

ser = serial.Serial('/dev/cu.usbmodem60A78A81',115200)  #60A78A81  open serial port
play = True
#Ciclo de muestreo 
while play:
    
    #
    ang = raw_input('Defina angulo , velocidad:')
    ser.write(ang)
    ser.write("\n\r")

    print ser.readline()
    if raw_input("Play again? ") == "n":
        break

 
#Cierre el puerto
ser.close()
