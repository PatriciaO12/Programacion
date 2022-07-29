# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:43:32 2022

@author: Renato
"""
import math
def DigitoIzquierda(n):
    while n>10:
        n=math.trunc(n/10)
    return n

x=int(input('Digite un número:'))
print('El primer dígito es:',DigitoIzquierda(x))

y=int(input('Digite un número:'))
print('El primer dígito es:',DigitoIzquierda(y))