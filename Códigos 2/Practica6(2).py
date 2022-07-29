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

for i in range(1,11):
 	print("\n",i*10,"|",end="   ")  # línea vertical
 	for j in range (1,t+1):
	  print(round((j*n)/(i*10),1),end="  ")

