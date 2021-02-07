# Script para mostrar el uso de los archivos 

archivo_entrada = open("../input/fahrenheit.txt","r")

datos = []

for line in archivo_entrada:
	print(line.strip())
	datos.append(line.strip())

print(datos)

archivo_entrada.close()

