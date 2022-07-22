# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:40:28 2022

@author: HP
"""

a=int(input('Ingrese las filas:'))
b=int(input('Ingrese las columnas:'))
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(i,end="")
    print()
        
for i in range(1,a+1):
    for j in range(i,0,-1):
        print(i,end="")
    print()