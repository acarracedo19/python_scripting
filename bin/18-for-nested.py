# Script para mostrar el uso de for anidado

lista_1 = ["Orisel", "Betzaida", "Manuel", "Jaime"]
lista_2 = ["Walter", "Orisel", "Jaime", "Karen"]

print("Contenido de lista_1:")
print(lista_1)
print("\nContenido de lista_2:")
print(lista_2)

for nombre_1 in lista_1:
	print("Recorriendo lista_1: " + nombre_1)
	for nombre_2 in lista_2:
		print("Recorriendo lista_2: " + nombre_2)
		if nombre_1 == nombre_2:
			print("--Encontre coincidencia: " + nombre_1)
