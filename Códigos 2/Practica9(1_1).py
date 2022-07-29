# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:46:43 2022

@author: Renato
"""

a=int(input('Ingrese el tamaño del vector:'))
vec1=[]
for i in range(a):
    vec1.append([0])
for i in range(a):
    vec1[i]=int(input('Elemento {}:'.format(i+1)))


b=int(input('Ingrese el tamaño del vector:'))
vec2=[]
for i in range(b):
    vec2.append([0])
for i in range(b):
    vec2[i]=int(input('Elemento {}:'.format(i+1)))

print('vec1:',vec1)
print('vec2:',vec2)

def comparar(vector1, vector2,t):
    iguales=0
    for i in range(t):
        if vector1[i]==vector2[i]:
            iguales=iguales+1
    return (iguales/t*100)

print('La similitud es:',comparar(vec1,vec2,len(vec1)))