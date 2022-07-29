# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 12:30:13 2022

@author: Dell
"""

def esprimo(num):
    contador = 0
    for i in range(1,num+1):
        if num% i==0:
            contador+=1
    if contador==2:
       return True
    else : 
        return False

for h in range(1,20):
     if esprimo(h+1):
         print(h+1,end=" ")
         
print()