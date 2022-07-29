# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 18:51:56 2022

@author: Renato
"""

base=exponen=0
while base<=0:
   base = int(input("Ingrese la base:"))

while exponen<=0:
   exponen = int(input("Ingrese el exponente:"))

resultado1=base**exponen
print("La potencia es:",resultado1)

resultado2=pow(base,exponen)
print("La potencia es:",resultado2)