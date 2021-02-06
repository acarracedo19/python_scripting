# Script para mostrar el uso de los archivos 

archivo_entrada = open("../input/fahrenheit_modificado.txt","r")

datos = []
suma = 0
promedio = 0
lineas_archivo = 0
contador_numeros = 0
contador_no_numeros = 0

for line in archivo_entrada:
	datos.append(line.strip())
	lineas_archivo += 1

archivo_entrada.close()

print(datos)

for valor in datos:
	if valor.isdigit():
		suma += int(valor)
		contador_numeros += 1
		print("--" + valor + " es un número")
	else:
		print("**" + valor + " NO es número")
		contador_no_numeros += 1

promedio = round(suma / len(datos),2)

print("\nEn el archivo se encontraron " + str(lineas_archivo) + " líneas en el archivo")
print("En el archivo se encontraron " + str(contador_numeros) + " números válidos, cuyo promedio es: " + str(promedio))
print("Se encontraron " + str(contador_no_numeros) + " valores no numéricos")
