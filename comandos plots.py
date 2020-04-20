# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:14:56 2019

@author: ferchi
"""
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

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

            
#plotear un texto:
plt.text(max(t)/8, max(d*10**12)*0.95, 'D= '+str("%.2f" %(D*10**12))+' $um^2$', horizontalalignment='center',verticalalignment='center')

#plots de 3D de colores (o sea la proyección 2D): Ejemplo de gaussiana (porque aguanten las gaussianas)
x=np.arange(-19,20,0.1)#defino x e y
y=np.arange(-19,20,0.1)
z=np.zeros((len(x),len(y)))
gaussiana= lambda x,y:np.exp(-np.sqrt((np.abs(vx**2)+np.abs(vy**2)))/10)

for i,vx in enumerate(x):#muy util usar enumerate
    for j,vy in enumerate(y):
        z[i,j]=gaussiana(vx,vy)#armo la matriz z con los valores z(x,y)

    

plt.contourf(x,y,z)
plt.colorbar() # :D, anda
        