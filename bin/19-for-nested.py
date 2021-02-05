# Script para mostrar el uso de for anidado

lista_cadenas = ["Primer cadena",
                 "Segunda linea",
                 "Estamos aprendiendo Python",
                 "y lo flexible",
                 "que es"
]

cantidad_espacios = 0

print(lista_cadenas)

for cadena_actual in lista_cadenas:
	for caracter_actual in cadena_actual:
		if caracter_actual == " ":
			cantidad_espacios += 1

cantidad_palabras = cantidad_espacios + len(lista_cadenas)

print("Hay " + str(cantidad_palabras) + " palabras en estas cadenas de texto")
