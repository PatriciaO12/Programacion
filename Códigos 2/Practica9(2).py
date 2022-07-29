# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 00:04:31 2022

@author: Renato
"""
import random
t=int(input('Ingrese el tamaño de la lista:'))
min=int(input('Ingrese el valor mínimo:'))
max=int(input('Ingrese el valor máximo:'))
vec=[]
for i in range(t):
    vec.append([0])
for i in range(t):
    vec[i]=random.randint(min, max)
print(vec)

for i in range(min, max+1):
    print('[',i,']:')
    
        