# Script para mostrar el uso de for each

lista_numeros = [91,92,93,94,95,96,97,98,99,100]
suma = 0

size_lista_numeros = len(lista_numeros)

for i in range(0,size_lista_numeros):
	numero_actual = lista_numeros[i]
	suma += numero_actual

print(suma / size_lista_numeros)

