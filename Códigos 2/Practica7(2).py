# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 19:10:04 2022
Tema: a^2+bx+c=0
@author: Renato
"""
import math
a = int(input("Ingrese a:"))
b = int(input("Ingrese b:"))
c = int(input("Ingrese c:"))

if a==0:
    print("No es ecuación de segundo grado")
else:
    D=pow(b,2)-(4*a*c)
    if D==0:
        x1=-b/(2*a)
        x2=x1
        print("x1:",x1,"  x2:",x2)
    elif D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print("x1:",x1,"  x2:",x2)
    else:
        r=(-b)/(2*a)
        i=math.sqrt(abs(D))/2*a
        print(r,"+",i,'i')
        print(r,"-",i,'i')