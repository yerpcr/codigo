import time 
import serial 
import os
nulo=b''
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

##bucle numero de analogos

while (True):
    variables = input("Digita el nombre de las veriables. Recuerda separar cada una de ellas con una coma:\n")
    n,o = cadena(variables)
    if (n>5):
        print("Recuerde que es un maximo de 5 analogos. Vuelvalo a intentar.\n")
    else:
        break

##fin bucle

o+="\n"
print ("Son "+str(n)+" variables: ")
file.write(o)
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=0.5)
test=0
print("Serial configurado\n")


##check
while(test!=n):
    ser.write(str.encode(str(n)))
    while (ser.inWaiting()):
        time.sleep(0.01)
    q=ser.readline()
    print (q)
    if (q!=nulo):
        test = int(q)
        print(test)
        ser.flush()

##fin check
print ("Inicio de datos")

a = time.time()
ent=""
print("ok\n")
while 1 :
    s = ser.readline()
    if (s==b'*'):
        ent+="\n"
        print (ent)
        file.write(ent)
        ent=""
    else:
        ent += "\t"
        ent += str(int(s))
        print (s)
