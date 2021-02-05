# Script para mostrar el uso de las listas

lista = [17, 12, 9, 18, 11, 19, 7, 13, 14, 16, 1, 10, 8, 4, 6, 3, 15, 2, 5, 20]
print(lista, ": Lista original")

lista.sort()
print(lista, ": Después de ordenar")

lista.append(21)
print(lista, ": Después de agregar el número 21")

otra_lista = [26, 22, 23, 24]
print(otra_lista, ": Valor de la otra_lista")

lista.extend(otra_lista)
print(lista, ": Después de agregar la otra_lista")

lista.insert(15,25)
print(lista, ": Después de agregar el valor 25 en el índice 15")

lista.remove(26)
print(lista, ": Después de eliminar el valor 26")

lista.sort()
print(lista, ": Después de ordenar nuevamente")
