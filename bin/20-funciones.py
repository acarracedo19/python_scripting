# Script para mostrar el uso de las funciones

def saluda(nombre):
	resultado = "Que onda " + nombre + " ¿todo bien?"
	return resultado

nombres = ["Zuleima","Nora","Francisco","Juan Carlos"]

for nombre in nombres:
	print(saluda(nombre))


