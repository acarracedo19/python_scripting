# Script para mostrar el uso del tipp de una variable y su impresión en pantalla

# Obten de la librería datetime lo que necesitamos para saber la fecha
from datetime import date
import random

# Crea una variable que almacene un entero al azar
numero_entero = random.randint(0,10)

# Crea una variable que almacene un flotante al azar
numero_flotante = random.uniform(0,10)

# Crea una variable que almacene la fecha del día
fecha_actual = date.today()

# Crea una variable tipo string
texto = "Aprendiendo Python"

# Crea una variable tipo Boolean
variable_logica = True

# Imprime el tipo de variables 
print(type(numero_entero))
print(type(numero_flotante))
print(type(fecha_actual))
print(type(texto))
print(type(variable_logica))
