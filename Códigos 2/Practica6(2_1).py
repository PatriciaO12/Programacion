# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:05:47 2022

@author: Renato
"""
n=t=0	#inicializo las variables '''
while n<=0:
	n=int(input("Tamaño del paquete: "))
while t<=0:
	t=int(input("Tamaño máximo de ventana de envío: "))

print("   |",end="")	
for i in range(1,t+1):   # etiqueta superior
	print(f"\t{n*i}",end="")
print()	
for i in range(1,t*10):   # línea horizontal
	print("-",end="")
print()
