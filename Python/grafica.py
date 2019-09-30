#E:\Drive\IdeAprende
import matplotlib.pylab as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d):
    return a * np.exp(-b * x) + c
def data(o):
    v = []
    dt=""
    for i in o:
        if (i=='\t' or i=='\n'):
            try:
                v.append(float(dt))
                print (dt,"OK")
            except:
                print (dt)
            dt=""
        else:
            dt+=i
    return (v)
datas=open('./doc/DatosPanel2.txt','r')

Values=[]
Corriente=[]
Tiempo=[]
c = 0
for i in datas.readlines():
    c+=1
    print (i,c)
    var=data(i)
    #Values.append([float(i[:var[0]]),float(i[var[0]+1:var[1]]),float(i[var[1]+1:])])
    try:
        Corriente.append(float(var[0]))
        Tiempo.append(float(var[1]))
    except:
        print (var)
datas.close()

I=np.array(Corriente[2000:])
t=np.array(Tiempo[2000:])

plt.xlabel('Tiempo(s)')
plt.ylabel('Corriente(mA)')
plt.plot(t,I,'.')
plt.show()

popt, pcov = curve_fit(func, VR, TC)
