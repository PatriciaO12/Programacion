# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:59:38 2022

@author: Renato
"""

n=int(input('Ingrese n:'))
sum=0
for i in range(1,n+1):
    sum=sum+pow(2,i)
print('La suma total es:',sum)
