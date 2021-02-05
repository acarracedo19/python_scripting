# Script para mostrar el uso de for each

cadena_texto = "En esta cadena de texto hay ocho palabras"
cantidad_espacios = 0

print(cadena_texto)

for caracter_actual in cadena_texto:
	if caracter_actual == " ":
		cantidad_espacios += 1

print("Hay " + str(cantidad_espacios + 1) + " palabras en la cadena de texto")

