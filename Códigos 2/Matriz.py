numfilas=[]
numcolumnas=[]

filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))

print("Rellene las columnas a:")
for i in range(columnas):
    print("Ingrese a",i+1)
    numcolumnas.append(int(input()))

print("Rellene las filas b:")
for i in range(filas):
    print("Ingrese b",i+1)
    numfilas.append(int(input()))

print("Matriz formada es: ")
print("\t\t",end="")
for i in range(columnas):
    print(numcolumnas[i],end="  ")
print("")
for i in range(columnas*3):
    print("---",end="")
print("")
for i in range(filas):
    print(numfilas[i]," |",end="\t")
    for j in range(columnas):
        producto=numfilas[i]*numcolumnas[j]
        if producto>9:
            print(producto,end = " ")
        else:
            print(producto,end="  ")

    print("")
