# Script para mostrar el uso de los archivos 

texto_1 = "Que ondas"
texto_2 = "Estamos aprendiendo"
texto_3 = "Python !!!"

archivo_salida = open("../output/texto.txt","w")

archivo_salida.write(texto_1 + "\n")
archivo_salida.write(texto_2 + "\n")
archivo_salida.write(texto_3)

archivo_salida.close()
