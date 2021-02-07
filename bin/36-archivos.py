# Script para mostrar el uso de los archivos 

archivo_entrada = open("../input/aeropuertos.txt","r")

datos = []

for line in archivo_entrada:
	print(line.strip())
	datos.append(line.strip())

archivo_entrada.close()

for dato in datos:
	analisis = dato.split(";")
	codigo = analisis[0]
	pais = analisis[1]
	nombre = analisis[2]
	ubicacion = analisis[3]

	print(codigo + "\t" + nombre + "\n\t" + pais)

