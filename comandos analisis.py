# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:14:20 2019

@author: ferchi
"""

#histogramas y estadistica de la manera correcta:

#hacer un histograma de un vector
#si es solo plotear
plt.hist(y,bins=numero_bins)

#si hace falta tener los valores
cant,bins=np.histogram(y,bins=num)
#por lo que entiendo, el vector bins te tira los bordes de los bins, lo que es al pedo asi que lo cambio para que tenga los centros
for i in range(len(bins)-1):
    bins[i]=(bins[i]+bins[i+1])/2
bins=bins[:-1]
plt.bar(bins,cant,width=0.8,align='center') #meter barras



#fiteo con la funcion f 

#valores iniciales
iniciales=np.array([1,0.1,1.6,0.45]) #crea un vector con los valores iniciales del fiteo en el orden de las variables de la funcion

parametros_optimizados, matriz_covarianza = curve_fit(f,x,y,p0=iniciales,sigma = ey,absolute_sigma=True) 
#calcula el fiteo y devuelve los sigmas y los valores de las variables que dan el fiteo, el sigma es el error del eje y. la parte del absolute_sigma es para que la matriz de error dependa del error de y, si es false depende de cuanto se dispersan del ajuste
#matriz_covarianza es una matriz que en su diagonal tiene los errores al cuadrado de cada parametro, el resto de la matriz la tenes que usar para propagar errores de manera correcta                  

#plotear el fiteo 
xx=np.linspace(min(x),max(x),1000) #vector auxiliar para que la funcion quede continua                
plt.plot(xx,f(xx, *parametros_optimizados), 'g-', label = 'Ajuste') #si no entendes que hace *parametros_optimizados anda a 'sintaxis basica y atajos de teclado utiles' 

#plotear con valores iniciales:
plt.plot(xx,f(xx, *iniciales), 'g-', label = 'Ajuste')

