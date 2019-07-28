import time 
import serial 
import os

file = open ("./doc/dia1.txt","w")

ser = serial.Serial('/dev/ttyUSB0',9600)
a = time.time()
while 1 :
    s = ser.readline()
    if s!='Hola':
        file.write(s+"\t"+str(time.time())+"\n")
        print(s+"\n")
    else: 
        print (s)

