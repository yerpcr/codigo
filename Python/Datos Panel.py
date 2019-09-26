import time
import serial
import os

r = 0
a = 110.0
b = 1023.0
c = 0.0
seg = 0
def main ():
    
    print("\n Hola, maestro. Podrias ayudarme con el nombre del archivo:\n")
    nombre = input()
    archivo = "./doc/"+str(nombre)
    archivo1 = open (archivo,"w")
    
    print("\nArchivo " + str(nombre) + " creado")    
    n_variables, v = Variables ()
    archivo1.write(str(v))
    puerto = input("Digite el numero del puerto:\t")
    arduino = serial.Serial( puerto, 9600, timeout=0.5)
    
    print("Serial configurado\n")
    
    envioVariables(n_variables,arduino)

    print ("Inicio de datos")
    fecha = time.ctime()
    seg = time.time()
    print (fecha)
    archivo1.write(str(fecha)+"\n")
    archivo1.close()
    entrada = ""
    pp = 0
    nulo = b''
    while True :
        archivo2 = open (archivo,'a')
        s = arduino.readline()
        if (s!=nulo):
            if (s == b'*\r\n'):
                entrada+="\t"
                tiempo = time.time()-seg
                entrada+=str(tiempo)
                entrada+="\n"
                print (entrada,"OK")
                archivo2.write(str(entrada))
                entrada = ""
            else:
                try:
                    x = (a*float(s)/b)+c
                except:
                    print ("\nProblema con el dato:",s)
                else:
                    entrada += "\t"
                    entrada += str(x)

def Variables():
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
    return(n,o)

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



main ()
