import serial
import time

def puertis(port):
    port = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=0)
    while True:
	print(port.read())
	time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

