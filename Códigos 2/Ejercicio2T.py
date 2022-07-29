import random

def rellenar(matriz):
	for i in range(11):
		matriz.append([])
		for j in range(8):
				if i==10:
					matriz[i].append(0)
				elif j==7:
					matriz[i].append(0)
				else:
					matriz[i].append(random.randint(0,100))
			
def totales(matriz):
	for i in range(10):
		suma=0
		for j in range(7):
			suma=suma+matriz[i][j]
		matriz[i][7]=round(suma/7,2)
	
	for i in range(8):
		suma=0
		for j in range(11):
			suma=suma+matriz[j][i]
		matriz[10][i]=round(suma/10,2)
				
			
def imprimir(matriz):
	print("\tN1    N2    N3    N4    N5    N6    N7    TOTAL")
	for i in range(11):
		if i==10:
			print("TOTAL",end="   ")
		else:
			print("M",i+1,end="\t")
		for j in range(8):
			if i==10:
				print(matriz[i][j],end="  ")
			else:
				if matriz[i][j]<10:
					print(matriz[i][j],end="     ")
				elif matriz[i][j]==100:
					print(matriz[i][j],end="   ")
				else:
					print(matriz[i][j], end="    ")
		print("")
		
def materiaMenos(matriz,opc):
	for i in range(10):
		if(matriz[i][7]<matriz[10][7]):
			if opc==1:
				print("La materia M",i+1)
			else:
				print("La materia M",i+1,"con promedio de",matriz[i][7])
				
def materiaMas(matriz):
	mayor=0
	materia=0
	for i in range(10):
		if (matriz[i][7]>mayor):
			mayor=matriz[i][7]
			materia=i
	print("La materia con mejor promedio es M",materia+1,"con promedio de ",mayor)
			
			
matriz=[]
rellenar(matriz)
totales(matriz)
print("Notas Generadas: ")
imprimir(matriz)
print("MENU")
print("1.Materia con peores calificaciones al promedio")
print("2.Nota de las peores calificaciones")
print("3.Materia con mejor promedio")
opc=int(input("Ingrese la opcion: "))
if opc==1:
	materiaMenos(matriz,opc)
elif opc==2:
	materiaMenos(matriz,opc)
elif opc==3:
	materiaMas(matriz)
else:
	print("No existe esa opcion")
			