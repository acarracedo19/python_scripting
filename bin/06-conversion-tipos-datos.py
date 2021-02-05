# Script para mostrar conversión de tipos de datos para ser impresos en pantalla

from datetime import date

# Define variables
entero = 8
flotante = 8.2
fecha = date.today()
boolean = False

entero_como_string = str(entero)
flotante_como_string = str(flotante)
fecha_como_string = str(fecha)
boolean_como_string = str(boolean)

# Imprime el valor de las variables y el tipo de las que se convirtieron a tipo "string"
print(entero,type(entero),entero_como_string,type(entero_como_string))
print("El valor de la variable: \"entero\" es: " + str(entero) + " y el de la variable \"entero_como_string\" es: " + entero_como_string +"\n")

print(flotante,type(flotante),flotante_como_string,type(flotante_como_string))
print("El valor de la variable: \"flotante\" es: " + str(flotante) + " y el de la variable \"flotante_como_string\" es: " + flotante_como_string +"\n")

print(fecha,type(fecha), fecha_como_string,type(fecha_como_string))
print("El valor de la variable: \"fecha\" es: " + str(fecha) + " y el de la variable \"fecha_como_string\" es: " + fecha_como_string + "\n")

print(boolean,type(boolean),boolean_como_string,type(boolean_como_string))
print("El valor de la variable: \"boolean\" es: " + str(boolean) + " y el de la variable \"boolean_como_string\" es: " + boolean_como_string + "\n")
