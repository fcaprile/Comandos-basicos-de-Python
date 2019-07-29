# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:28:04 2017

@author: ferchi
"""

#paquetes:
import math as m
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from array import array
import os
import sys
from scipy.integrate import quad as inte


#Carpetas y demas:
#asi se escriben los directorios de las carpetas:
carpeta='C:/Users/ferchi/.spyder-py3/labo/laser/fotos/'

#armar un vector con todos los archivos que terminan con ".txt" en una carpeta:                       
lista=[]
for archivo in os.listdir(carpeta):
    if archivo.endswith(".txt"):
        lista.append(archivo)


#cargar txt:
d=np.loadtxt('d1.txt', delimiter = '\t')#\t es qeu los divide por tab los valores
#SI LOS DATOS VIENEN CON LOS DECIMALES SEPARADOS POR COMAS EN VEZ DE PUNTOS (si no es asi, ignorar):
a=0
while i<40: #en vez de 40 va la cantidad de txts   
    a1 = open(carpeta+str(a)).read().replace(',','.')#cambio las comas por puntos y lo guardo como b
    a1=a1.split()#convierto v en una matriz separando todo por tabs y enters, por eso esta el ()
    #saco la parte que dice time, date, etc
    a1.remove(a1[0])
    a1.remove(a1[0])
    a1.remove(a1[0])
    a1.remove(a1[0])
    #separo el eje x del y
    x=a1[::2]#agarro las columnas pares
    y=a1[1::2]#agarro las columnas impares
    #lo convierto de texto a numeros
    for i in range(len(x)):
        x[i]=float(x[i])
        y[i]=float(y[i])
    a1=np.zeros((len(x),2))
    a1[:,0]=x
    a1[:,1]=y
    #lo reescribo
    np.savetxt(str(a)+'.txt',a1, fmt='%.18g', delimiter='\t', newline=os.linesep)        
    a=a+1



    #Vectores y matrices:
#crear una matriz de ceros de 1x2:
m=np.zeros((1,2))


#seleccionar desde el elemento número a hasta el numero b del vector x
x=x[a:b]

#seleccionar columna i:
xi=x[:,i]

#borrar elemento
del y[2]#si no es .np
x=np.delete(x,0)#si es .np
           
for i in range(10):
    e0=np.delete(e0,-1)#si es .np
    m0=np.delete(m0,-1)#si es .np
    ee0=np.delete(ee0,-1)#si es .np
    em0=np.delete(em0,-1)#si es .np

#agregar elementos
a=np.append(a,1)#le agrego al vector a el numero 1

#trasponer la matriz
a=np.transpose(a)          
           
#definir vectores hechos por valores equiespaciados
x=np.linspace(0,1,100)#100 valores entre el 0 y el 1
y=np.linspace(0,2,100)

#remover valores "nan":
d = d[~np.isnan(d)]
t = t[~np.isnan(t)]
        
#usar un numero con solo 2 decimales:
x="%.2f" %x# x es el numero

#juntar 2 arrays:
z = np.concatenate((x, y), axis = 0)

#ordenar una matriz cosa que los valores vayan de menor a mayor en base a la 1º fila:
#esto lo tuve que usar 1 vez y estuve 45 min para lograrlo, por algun motivo solo funciona si lo ordena por columnas, asi que la doy vuelta, la ordeno y la vuelvo a dar vuelta, ojala nunca lo tengas que usar:
#si tus vectores son x2 e y2 y queres ordenar el vector x:
A2=np.array([x2,y2])
A2=np.transpose(A2)
A2=A2[A2[:,0].argsort()]
A2=np.transpose(A2)#dificil de creer pero funciona


#definir una funcion rapido:
f=lambda variable1,variable2,variable3,variable4: (variable1)^2-variable2+variable3*variable4

#definir una funcion lento:
def f(x,y):
    z=x+y
    w=x+z
    return w    #z no queda guardado
                                                  
   

                                               
#Plotear y fitear y mucho mas:
        
#config ploteo que queda grande que se ve el texto y queda bien ajustado
plt.rcParams['font.size']=20#tamaño de fuente
plt.figure(num=0, figsize=(9,6), dpi=80, facecolor='w', edgecolor='k')
plt.subplots_adjust(left=0.14, bottom=0.13, right=0.98, top=0.98, wspace=None, hspace=None)

#plotear (graficar)
plt.plot(x,y,'b*', label = 'Datos')#x e y deben ser vectores del mismo tamaño
plt.errorbar(x,y,ey,linestyle = 'None')
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best') 

#usar scatter para plotear (queda distinto y con puntitos):
plt.scatter(x,y,s=100,c='g',marker='-', label = 'v teorica 1')

#subplots(varios plots en la misma ventana)
plt.subplot(2,1,1)
plt.plot(x,y,'b*', label = 'Datos')#x e y deben ser vectores del mismo tamaño
plt.subplot(2,1,2)
plt.plot(x,y,'b*', label = 'Datos')#x e y deben ser vectores del mismo tamaño

#escala logaritmica:
plt.semilogx()#escala logaritmica en x

            
#fiteo con la funcion f 
iniciales=np.array([1,0.1,1.6,0.45]) #crea un vector con los valores iniciales del fiteo en el orden de las variables de la funcion
popt, pcov = curve_fit(f,x,y,p0=iniciales,sigma = ey,absolute_sigma=True) #calcula el fiteo y devuelve los sigmas y los valores de las variables que dan el fiteo, el sigma es el error del eje y. la parte del absolute_sigma es para que la matriz de error dependa del error de y, si es false depende de cuanto se dispersan del ajuste
#popt son los valores de los parametros que devuelve el ajuste, pcov es una matriz que en su diagonal tiene los errores al cuadrado de cada parametro                      
                      
#plotear el fiteo 
xx=np.linspace(min(x),max(x),1000)#vector auxiliar para que la funcion quede continua                
plt.plot(xx,f(xx, *popt), 'g-', label = 'Ajuste')#los popt son los valores de las variables fiteadas que usara la funcion f                      

#plotear con valores iniciales:
plt.plot(xx,f(xx, iniciales[0], iniciales[1],iniciales[2],iniciales[3]), 'g-', label = 'Ajuste')#los popt son los valores de las variables fiteadas que usara la funcion f                      
       
#calcular R^2 y Chi cuadrado
residuals = y- f(x, popt[0],popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
chi=np.sum(((residuals/(ey))**2)/len(y))
print(r_squared,chi)

#guardarse los valores calculados en un txt
mat=np.zeros((len(popt)+1,2))
for i in range(len(popt)):
    mat[i,0]=popt[i]
    mat[i,1]=np.sqrt(pcov[i,i])
    
mat[-1,0]=r_squared
mat[-1,1]=chi
np.savetxt('C:/Users/ferchi/.spyder-py3/ajustes/'+'campo'+'.txt',mat, fmt='%.18g', delimiter='\t', newline=os.linesep)


       
#plotear un texto:
plt.text(max(t)/8, max(d*10**12)*0.95, 'D= '+str("%.2f" %(D*10**12))+' $um^2$', horizontalalignment='center',verticalalignment='center')

#hacer un histograma al vector y con una cantidad num de bins
#si es solo plotear
plt.hist(y,bins=num)

#si hace falta tener los valores
cant,bins=np.histogram(y,bins=num)
#por lo que entiendo, el vector bins te tira los bordes de los bins, lo que es al pedo asi que lo cambio para que tenga los centros
for i in range(len(bins)-1):
    bins[i]=(bins[i]+bins[i+1])/2
bins=bins[:-1]
plt.bar(bins,cant,width=0.8,align='center') #meter barras

#histograma con numeros enteros:
numeros=np.arange(min(a)-0.5,max(a)+1.5,1)
cant,bins=np.histogram(a,bins=numeros)

for i in range(len(bins)-1):
    bins[i]=(bins[i]+bins[i+1])/2
bins=bins[:-1]

plt.bar(bins,cant,width=0.9,align='center',label='Simulación',color='blue')

#○integrar algo:
scipy.integrate.quad(lambda x:f(x),-50,50)
#o si no:
inte(lambda x:f(x),-50,50)#con el inte que cargue al inicio
       
#guardar una imagen:
plt.savefig(carpeta+archivo+'.png')
            
#medir el tiempo:
start_time = time.time()
print('Tiempo transcurrido para el método 2: ', "%.2f" %float(time.time() - start_time),'segundos')

#%%
def posicion_x(x,valorx):
    posicion_x=np.where(abs(x-valorx)==min(abs(x-valorx)))[0][0]
    return posicion_x

def y_dado_x(x,y,valorx):
    pos=posicion_x(x,valorx)
    return y[pos]

def ajustar_entre(f,x,y,ey,xinf,xsup,escalax=1,escalay=1,color='g',label='Ajuste',plot=True):
    a=posicion_x(x,xinf)
    b=posicion_x(x,xsup)    
    y=y[a:b]
    x=x[a:b]
    ey=ey[a:b]
    popt, pcov = curve_fit(f,x,y,sigma =ey)
    if plot==True:
        xx=np.linspace(min(x),max(x),1000)                    
        plt.plot(xx*escalax,f(xx, *popt)*escalay, color=color, label = label)#los popt son los valores de las variables fiteadas que usara la funcion f                      
    return popt,pcov

def vector_entre(x,xinf,xsup):
    a=posicion_x(x,xinf)
    b=posicion_x(x,xsup)    
    return x[a:b]    



