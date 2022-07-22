
"""
Created on Thu Jul 21 20:57:45 2022

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
		
def rellenar(vector,n,vprimos):
	i=0
	j=0
	for i in range (n-1):
		vector.append(random.randint(1,40))
	print("El vector es: ")
	for j in range (n):
		print(vector[j])
		if primo(vector[j])==True:
			vprimos.append(vector[j])

def primo(num):
	for n in range(2,num):
		if num%n == 0:
			return False
	return True
	
	
n=int(input("Ingrese el valor: "))
if validar(n)==True:
	primos=[]
	vector=[n]
	rellenar(vector,n,primos)
	if len(primos)==0:
		print("No existen numeros primos")
	else:
		i=0
		print("Los numeros primos son: ")
		for i in range(len(primos)):
			print(primos[i])