import time 
import serial 
import os


def main ():
    
    archivo1 = crearArchivo()
    n_variables = Variables (archivo1)

    puerto = input("Ingrese el nombre del puero:\n")
    arduino = serial.Serial(puerto,9600,timeout=0.5)
    
    print("Serial configurado\n")
    
    envioVariables(n_variables,arduino)

    print ("Inicio de datos")
    a = time.time()
    ent=""
    while True :
        ent=entradaDatos(arduino,ent,archivo1)

def crearArchivo():
    print("\n Hola, maestro. Podrias ayudarme con el nombre del archivo:\n")
    nombre = input()
    archivo = "./doc/"+str(nombre)
    file = open (archivo,"w")
    print("\nArchivo " + str(nombre) + " creado")    
    return(file)

def Variables(file):
    while (True):
        variables = input("Digita el nombre de las veriables. Recuerda separar cada una de ellas con una coma:\n")
        n,o = cadena(variables)
        if (n>6):
            print("Recuerde que es un maximo de 6 analogos. Vuelvalo a intentar.\n")
        else:
            break

    ##fin bucle

    o+="\n"
    print ("Son "+str(n)+" variables: ")
    file.write(o)
    return(n)

def envioVariables(n,ser):
    nulo = b''
    test = 0
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

def entradaDatos(ser,entrada,file):
    s = ser.readline()
    if (s==b'*\r\n'):
        entrada+="\n"
        print (entrada)
        file.write(entrada)
        entrada=""
    else:
        entrada += "\t"
        entrada += str(int(s))
        print (s)
    return(entrada)

main ()
