# Script para mostrar el uso de las funciones relacionadas a strings

def string_finder(target_string,search_string):
    size = len(target_string)
    size_search = len(search_string)
    if search_string in target_string:

        ubicacion = target_string.find(search_string)
        final = ubicacion + size_search

        if ubicacion == 0:
            return "Al comienzo"
        if final == size:
            return "Al final"
        else:
            return "En medio"
        
    else:
        return "No encontrado"


print(string_finder("Copa Airlines", "Copa"))
print(string_finder("Copa Airlines", "nes"))
print(string_finder("Copa Airlines", "Air"))
print(string_finder("Copa Airlines", "Wingo"))
