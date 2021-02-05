# Script para mostrar el uso de operadores lógicos

# Crea una primer variable que almacene un entero
variable_1 = 4

# Crea una segunda variable que almacene un entero
variable_2 = 7

# Crea una tercera variable que almacene un entero
variable_3 = 5

# Crea variables tipo Boolean
onList = True
inStock = True
onSale = False
rotten = False

# Imprime los resultados de algunas condiciones logicas
print(variable_3 == variable_1)
print(variable_2 > variable_1 + variable_3)
print(variable_1 < variable_2)

print("")
print(onList and inStock)
print(onList and onSale)
print(onSale and rotten)
print(onList and inStock and onSale)
print(onList and inStock and onList)
