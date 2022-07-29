# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:28:04 2022

@author: Renato
"""

n=0
while(n<=0):
    n = int(input("Ingrese un número:"))
a=n
for i in range(n,0,-1): 
    print()
    for j in range (1,a+1):
        print(i,end="")
    a-=1
#endfor

for i in range(2,n+1): 
    print()
    for j in range (1,i+1):
        print(i,end=" ")
#endfor
