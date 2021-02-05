# Script para mostrar el uso de los archivos 

entero_1 = 78
entero_2 = 90
entero_3 = 16

archivo_salida = open("../output/enteros.txt","a")

print(str(entero_1), file = archivo_salida)
print(str(entero_2), file = archivo_salida)
print(str(entero_3), file = archivo_salida)

archivo_salida.close()
