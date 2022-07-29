import numpy as np

f=0
c=0
mayor=0


while (f<4 or f>30 ) or (c<4 or c>30):
    print("Ingrese los valores, deben ser mayores a 4 y menores que 30: ")
    f=int(input("Ingrese el número de filas de la matriz : "))
    c=int(input("Ingrese el número de columnas de la matriz: "))


vector=np.random.randint(1,high=1000,size=(f,c))

print(vector)

for i in range (f):
    for j in range (c):
        if vector[i][j]>mayor:
            mayor=vector[i][j]
            fila=i+1
            columna=j+1

print("El numero mayor de la matriz es :",mayor,"Se encuentra en la posición : [",fila,",",columna,"]")      
