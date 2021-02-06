# Script para mostrar el uso de los diccionarios

def cuenta_nombres(lista):

    variable = ""
    diccionario_nombres = {}

    for linea in lista:

        variable = linea.split(" ")

        if variable[0] in diccionario_nombres:
            diccionario_nombres[variable[0]] += 1
        else:
            diccionario_nombres[variable[0]] = 1

    return diccionario_nombres


lista_nombres = ["José Sánchez", "David Arana", "José Díaz",
             "David García", "José Barrios", "Julio Adames",
             "Francisco Galagarza", "Rafael Samudio", "Damian Muñoz",
             "Rafael Sinclair", "Julio Toro"]

print(cuenta_nombres(lista_nombres))

