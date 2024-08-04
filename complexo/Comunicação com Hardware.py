import serial
import time

arduino = serial.Serial(port='COM19', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    angle = input("Enter angle (0-180): ")
    value = write_read(angle)
    print(value)
