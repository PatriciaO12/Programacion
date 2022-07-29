# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:05:54 2022

@author: Renato
"""

A = [
    [1, 2, 3],
    [4, 5, 6],
]
B = [
    [5, -1],
    [1, 0],
    [-2, 3],
]
C=[]
for i in range(len(A)):
    C.append([])
    for j in range(len(B[0])):
        C[i].append(None)
        
#Multiplicación
for c in range(len(B[0])):
    for i in range(len(A)):
        suma = 0
        for j in range(len(A[0])):
            suma += A[i][j]*B[j][c]
        C[i][c] = suma
      
        
def Imprimir(A):
    print()
    for i in A:
        print("[ ",end="")
        for j in i:
            print("{}".format(j),end=" ")
        print("]")
    print()    
Imprimir(A)
Imprimir(B)
Imprimir(C)