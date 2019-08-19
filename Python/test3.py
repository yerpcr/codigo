import time 
import serial 
import os

print("\n Hi, master. Could you help me with the file's name:\n")
nombre = input()
archivo = "./doc/"+str(nombre)
file = open (archivo,"w")
print("\nFiles " + str(nombre) + " created")

ser = serial.Serial('/dev/ttyO2',9600)
a = time.time()
while 1 :
    s = ser.readline()
    if s!='Hola':
        texto = str(int(s)) + "\t" + str (time.time()) + "\n"
        file.write(texto)
        print(texto)
    else: 
        print (s)

