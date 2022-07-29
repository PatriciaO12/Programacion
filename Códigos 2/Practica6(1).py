# -*- coding: utf-8 -*-
"""
Created on Mon May 30 14:50:13 2022

@author: Renato
"""

n=0
while n<=0:
    n = int(input("Ingrese un entero:"))
for i in range(1,n+1): 
    res=0
    aux=1
    for j in range(1,i+1):
            res+=aux
            aux+=2;        
    print (f"{i}^2 = {res}")

