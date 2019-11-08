# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:14:20 2019

@author: ferchi
"""
from scipy.stats import chi2
from scipy.optimize import curve_fit
import numpy as np
#histogramas y estadistica de la manera correcta:

'''    
COMO HACER UN TEST CORRECTO DE LA BONDAD DEL AJUSTE:
en internet hay un monton de cosas de que es el chi^2 que estan MAL, lamentablemente. 
es heavy que sea tan asi pero bueno, lo que te dan es el R^2 que no es una buena medida de que tan bueno es un ajuste
un buen estimador es el chi cuadrado posta y es el siguiente: (para mas info consultar a alguien que cursara estadistica del df o probablemente en la de compu tambien lo vean)
'''    
def test_chi2(f,x,y,ey,parametros_ajustados=[]):
    '''
    f es la fucnion con la que ajustaste, x,y lo que mediste y ey el error con el que lo mediste 
    (si no te pusiste a caracterizar el error lee abajo la parte de desviacion standard)
    parametros_ajustados son los valores que te da el ajuste
    '''
    n=len(parametros_ajustados)
    N=len(y)
    if n==0: #si la f no viene de un ajuste
        t=np.sum((y-f(x)/ey)**2) #t es el nombre teorico que se le da al resultado de esa cuenta, no tiene nada que ver con el tiempo
    else:
        t=np.sum((y-f(x,*parametros_ajustados)/ey)**2)
        #para ser rigurosos, esto funciona si f es lineal en los parámetros (no la definiste como algo que depende de A**2), pero bue
    
    p_valor=1-chi2.cdf(t,N-n)
    return p_valor  #si p-valor es menor a tu significancia (se suele usar 0.05 por motivos nefastos), se rechaza la hipotesis de que f sea la funcion posta  
    
          
#desviacion estandard: (util para estimar el error en algo que mediste varias veces)
#"y" es una tanda de N valores que mediste al realizar siempre el mismo experimento:
#error al medir 1 vez:
ey=np.std(y,ddof=1) #lo de ddof es por temas teóricos

#error para el valor medio de tus N mediciones
e_media=np.std(y,ddof=1)/np.sqrt(N)
         
#hacer un histograma de un vector "y"
#si es solo plotear
plt.hist(y,bins=numero_bins)

#si hace falta tener los valores
n,bins=np.histogram(y,bins=numero_bins, density=True)#n son las alturas, bins son los bordes de los bins, density hace que todo este normalizado
dx=bins[1]-bins[0]
bins=bins[:-1]+dx/2#como eran los bordes, los centro
plt.bar(bins,n,width=dx)

#calculo y ploteo correcto del error de cada bin:
    
#si el histograma esta normalizado (si pusiste density=True):
N=len(y)
plt.errorbar(bins,n,np.sqrt(n/N)/dx,color='k',linestyle = 'None')#para curisosos: lo que se asume en este calculo es una distribucion estadistica que se llama "poisonniana" por si te interesa preguntarle a alguien que sepa o leer al respecto

#si el histograma NO esta normalizado (si pusiste density=False):
plt.errorbar(bins,n,np.sqrt(n)/dx,color='k',linestyle = 'None')#para curisosos: lo que se asume en este calculo es una distribucion estadistica que se llama "poisonniana" por si te interesa preguntarle a alguien que sepa o leer al respecto


            
            
            
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


#funciones que hice por mi cuenta que me sirven:

    
#ordenar una matriz cosa que los valores vayan de menor a mayor en base a la 1º fila:
#esto lo tuve que usar 1 vez y estuve 45 min para lograrlo, por algun motivo solo funciona si lo ordena por columnas, asi que la doy vuelta, la ordeno y la vuelvo a dar vuelta, ojala nunca lo tengas que usar:
#si tus vectores son x e y y queres ordenar en base al vector x:  
def ordenar(x,y):
    A2=np.array([x,y])
    A2=np.transpose(A2)
    A2=A2[A2[:,0].argsort()]
    A2=np.transpose(A2)#dificil de creer pero funciona
    return(A2)
    
    
def posicion_x(x,valorx):#dado un valor de x, te dice la posicion mas cercana
    posicion_x=np.where(abs(x-valorx)==min(abs(x-valorx)))[0][0]
    return posicion_x

def y_dado_x(x,y,valorx):#dado un valor de x, te dice el valor que corresponde en y
    pos=posicion_x(x,valorx)
    return y[pos]

def vector_entre(x,xinf,xsup):#vector entre 2 valores, x debe estar ordenado
    a=posicion_x(x,xinf)
    b=posicion_x(x,xsup)    
    return x[a:b]    

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


    
