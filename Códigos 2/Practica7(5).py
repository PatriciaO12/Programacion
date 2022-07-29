# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 12:28:35 2022

@author: Renato
"""
import math
x=int(input('Ingrese x:'))
n=int(input('Ingrese n:'))
sum=0
pot=2
for i in range(1,n+1,2):
    sum=float(sum+((-1)**(pot))*((x**i)/math.factorial(i)))
    pot=pot+1
print('La suma total es:',sum)
