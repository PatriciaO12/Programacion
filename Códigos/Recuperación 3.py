# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:09:06 2022

@author: Patricia Ocaña
"""

import random
def validar(num):
	if num>=4 and num<=30:
		print("Valor valido")
		return True
	else:
		print("Valor invalido")
		return False
		
def rellenar(matriz,n):
	for i in range(n+1):
		matriz.append([])
		for j in range(n+1):
				if i==n:
					matriz[i].append(0)
				elif j==n:
					matriz[i].append(0)
				else:
					matriz[i].append(random.randint(0,100))
					
def totales(matriz,n):
	for i in range(n):
		suma=0
		for j in range(n):
			suma=suma+matriz[i][j]
		matriz[i][n]=round(suma/n,2)
	for i in range(n+1):
		suma=0
		for j in range(n+1):
			suma=suma+matriz[j][i]
		matriz[n][i]=round(suma/n,2)

def imprimir(matriz,n):
	for i in range(n+1):
		print(" ",end="")
		for j in range(n+1):
			if j==n:
				print("TOTAL",matriz[i][j],end="  ")
			elif i==n:
				print("TOTAL",matriz[i][j],end="  \t ")
			else:
				if matriz[i][j]<10:
					print(matriz[i][j],end="   \t\t  ")
				elif matriz[i][j]==100:
					print(matriz[i][j],end=" \t\t  ")
				else:
					print(matriz[i][j], end="\t  \t  ")
		print("")


n=int(input("Ingrese el valor de N: "))
if validar(n)==True:
	matriz=[]
	rellenar(matriz,n)
	totales(matriz,n)
	imprimir(matriz,n)