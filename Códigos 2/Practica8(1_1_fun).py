# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:52:55 2022

@author: Renato
"""
def Area(base, altura):
    a=(base*altura)/2
    return a

b=int(input('Ingrese la base:'))
h=int(input('Ingrese la altura:'))
Respuesta=Area(b,h)
print('EL área del triángulo es:', Respuesta)
print('El resultado es:',Area(3,5))
