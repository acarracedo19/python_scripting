# Script para mostrar el uso de las listas

def promedio(lista):
	suma = 0
	for numero in lista:
		suma += numero
	return suma / len(lista)

lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_2 = [97, 87, 91, 83, 85, 91, 95, 99, 81, 85]

print ("El promedio de \"lista_1\" es:", promedio(lista_1))
print ("El promedio de \"lista_2\" es: " + str(promedio(lista_2)))
