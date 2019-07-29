# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:13:36 2019

@author: ferchi
"""
import numpy as np

#crear una matriz de ceros de 1x2:
m=np.zeros((1,2))


#seleccionar desde el elemento número a hasta el numero b del vector x
x=x[a:b]

#seleccionar columna i:
xi=x[:,i]

#borrar elemento
del y[2]#si no es .np
x=np.delete(x,0)#si es .np

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


#saber el tamaño de algo
tupla_de_tamaño=np.shape(matriz)#una tupla es un vector que no podes modificar

#ordenar una matriz cosa que los valores vayan de menor a mayor en base a la 1º fila:
#esto lo tuve que usar 1 vez y estuve 45 min para lograrlo, por algun motivo solo funciona si lo ordena por columnas, asi que la doy vuelta, la ordeno y la vuelvo a dar vuelta, ojala nunca lo tengas que usar:
#si tus vectores son x e y y queres ordenar en base al vector x:  
def ordenar(x,y):
    A2=np.array([x,y])
    A2=np.transpose(A2)
    A2=A2[A2[:,0].argsort()]
    A2=np.transpose(A2)#dificil de creer pero funciona
    return(A2)
