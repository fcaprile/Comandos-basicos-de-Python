# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 00:02:53 2019

@author: ferchi
"""
import numpy as np

tabulear varias filas: seleccionar varias filas + tab
sacar tab varias filas: seleccionar varias filas + shift + tab
comentar varias filas con '#': seleccionar varias filas + ctrl + 1
escribir comentario en varias filas: 

    

'''
texto
'''

separar codigo para correr con ctrl + enter:
#%%

definir funciones:
f=lambda x,A,y0: x*A+y0

def f(x,A,y0):
    return(x*A+y0)

como hacer de manera un poco más eficiente un for
NO:
for i in range(len(a)):
    for j in range(len(b)):
        print('así no')
#pasa que calcular la len de algo toma tiempo        

SÍ:
len_a=len(a)
len_b=len(b)
    
for i in range(len_a):
    for j in range(len_b):
        print('así sí')
#tambien podia empezar con len_a,len_b=np.shape([a,b])



dar como parametro a una funcion un array entero: *array
ejemplo:
def f(a,b,c,d):
    return(a+b+c+d)
parametros=np.array([1,2,3])
print(f(2,*parametros))

#medir el tiempo:
start_time = time.time()
print('Tiempo transcurrido para el método 2: ', "%.2f" %float(time.time() - start_time),'segundos')

