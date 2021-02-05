# Script para mostrar el uso de las funciones relacionadas a strings

def numero_palabras(texto):
    return len(texto.split(" "))

print(numero_palabras("estamos, aprendiendo, python"))
print(numero_palabras("Que ondas!"))
print(numero_palabras("habraespaciosenestaoracion"))
