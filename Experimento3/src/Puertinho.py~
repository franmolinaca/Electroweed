import serial
import time

def puertis(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch=='\r' or ch=='':
            return rv

port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=0)

while True:
    port.write("\r\nDiga algo:")
    rcv = readlineCR(port)
    port.write("\r\nMe llega:" + repr(rcv))

