# Script para mostrar el uso de los diccionarios

def nominaciones_oscares(diccionario_nominados):
    nombre = ""
    maximo = 0

    for nominados in diccionario_nominados.keys():

        print(nominados)

        if diccionario_nominados[nominados] > maximo:
            nombre = nominados
            maximo = diccionario_nominados[nominados]

    return (nombre,maximo)


nominados = {'Marlon Brando': 8, 'Denzel Washington': 8, 'Jack Nicholson': 12, 'Meryl Streep': 21, 'Al Pacino': 9}
print(nominaciones_oscares(nominados))
