# Reto 12

# Escribe una función que se llame "password_check" que tome 1 parámetro:
# una cadena de texto (string)

# La función debe regresar un valor Booleano:
# True si el password es válido y False sino

# Las reglas son:
# - 8 caracteres mínimo
# - Debe contener al menos 1 caracter de las siguientes categorías: mayúscula, minúscula, número y
#   solo los siguientes signos de puntuación: !@#$%&()-_[]{};':",./<>?

# A partir de esta línea indica como resolverías el reto.

# Escribe aquí tu funcion



print(password_check("tHIs1sag00d.p4ssw0rd.")) # El script regresará True
print(password_check("3@t7ENZ((T")) # El script regresará True
print(password_check("2.shOrt")) # El script regresara False
print(password_check("all.l0wer.case")) # El script regresará False
print(password_check("inv4l1d CH4R4CTERS~")) # El script regresará False


