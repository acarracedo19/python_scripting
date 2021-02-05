# Script para mostrar el uso de los archivos 

lista = ["Betzy","Orisel","Yhonattan","Manuel","Jose","Priscilla","Zuleima","Javier","Jaime","Nora","Carlos"]

archivo_salida = open("../output/nombres.txt","w")

for nombre in lista:
   print(nombre, file = archivo_salida)

archivo_salida.close()
