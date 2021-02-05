# Script para mostrar el uso de los archivos 

entero_1 = 12
entero_2 = 34
entero_3 = 56

archivo_salida = open("../output/enteros.txt","w")

archivo_salida.write(str(entero_1))
archivo_salida.write(str(entero_2))
archivo_salida.write(str(entero_3))
archivo_salida.write("\n")
archivo_salida.close()
