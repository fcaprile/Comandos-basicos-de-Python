# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:56:04 2019

@author: ferchi
"""

import numpy as np
import os
import sys

#asi se escriben los directorios de las carpetas:
carpeta_laser='C:/Users/.spyder-py3/labo/laser/fotos/'

#armar un vector con todos los archivos que terminan con ".txt" en una carpeta:                       

def armar_ista(carpeta):
    lista=[]
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            lista.append(archivo)
    return(lista)

lista=armar_lista(carpeta_laser)


#uso de string y float:
a=10
a_string=str(a) 
a_float=float(a)
a_int=int(a)


#cargar y guardar txt:
    
#opcion numpy: rapida, funciona con los decimales separados por puntos
d=np.loadtxt('nombre.txt', delimiter = '\t')#\t es que los divide por tab los valores
np.savetxt('nombre.txt',a1, fmt='%.18g', delimiter='\t', newline=os.linesep)        
#en caso que vengan divididos por comas:
def cambiar_comas_por_puntos(carpeta,nombre):
    a1 = open(carpeta+nombre).read().replace(',','.')#cambio las comas por puntos y lo guardo como b
    a1=a1.split()#convierto v en una matriz separando todo por tabs y enters, por eso esta el ()
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
    np.savetxt(nombre,a1, fmt='%.18g', delimiter='\t', newline=os.linesep)        

#opcion gentxt: no la conozco tanto, parece mas robusta
np.gentxt('nombre.txt', delimiter = '\t')

            