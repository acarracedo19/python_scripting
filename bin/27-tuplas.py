# Script para mostrar el uso de las tuplas

def info(caracter):
    tipo = ""

    if ord(caracter) >= 48 and ord(caracter) <= 57:
        tipo = "número"
    elif (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
        tipo = "letra"
    else:
        tipo = "puntuación"

    return (caracter,ord(caracter),tipo)

print(info("q"),type(info("q")))
print(info("7"),type(info("7")))
print(info("`"),type(info("`")))
