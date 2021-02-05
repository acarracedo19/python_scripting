# Script para mostrar el uso de las listas

def promedio_2D(lista):
    resultado = []

    for numero_en_lista in lista:
        print("--",numero_en_lista)
        suma = 0

        for numero in numero_en_lista:
            print("valor:",numero)
            suma += numero
            print("suma:",suma)

        resultado.append(suma / len(numero_en_lista))
        print("*** Promedio",suma / len(numero_en_lista))
        print("\n")
    return resultado

lista_numeros = [[91, 95, 89, 92, 85],
          [85, 87, 91, 81, 82],
          [79, 75, 85, 83, 89],
          [81, 89, 91, 91, 90],
          [99, 91, 95, 89, 90]]

resultados_promedios = promedio_2D(lista_numeros)

print("Lista de números: ", lista_numeros)
print("Promedios de la lista \"lista_numeros\": ", resultados_promedios)
