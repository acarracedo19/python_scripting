# Script para mostrar el uso de las funciones

def invertido(texto):
	texto_invertido = ""

	for i in range(len(texto)-1, -1, -1):
		texto_invertido += texto[i]
	return texto_invertido


texto = "Este texto se invertira!"
print(texto)

texto_final = invertido(texto)
print(texto_final)
