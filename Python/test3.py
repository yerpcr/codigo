import time 
import serial 
import os

def cadena (entrada):
    i=1
    salida =""
    for x in range (0,len(entrada)):
        if (entrada[x]==","):
            i=i+1
            salida += "\t"
        else:
            salida += entrada[x]
    return (i,salida)

print("\n Hola, maestro. Podrias ayudarme con el nombre del archivo:\n")
nombre = input()
archivo = "./doc/"+str(nombre)
file = open (archivo,"w")
print("\nFiles " + str(nombre) + " created")
while (True):
    variables = input("Digita el nombre de las veriables. Recuerda separar cada una de ellas con una coma:\n")
    n,o = cadena(variables)
    if (n>5):
        print("Recuerde que es un maximo de 5 analogos. Vuelvalo a intentar.\n")
    else:
        break
print ("Son "+str(n)+" variables:\n")
file.write(o)
ser = serial.Serial('/dev/ttyO2',9600)
ser.write(n)
a = time.time()
while 1 :
    s = ser.readline()
    if s!='Hola':
        texto = str(int(s)) + "\t" + str (time.time()) + "\n"
        file.write(texto)
        print(texto)
    else: 
        print (s)

