# Reto 1
# Calcula la diferencia entre dos fechas dadas donde lo que variará serán el número del mes y el día
from datetime import date
import random

# Define variables, favor no tocar nada en esta dos líneas
# Que lo que hacen es crear 2 fechas

fecha_inicial = date(date.today().year,random.randint(1,11),random.randint(1,28))
fecha_final = date(date.today().year,fecha_inicial.month,random.randint(fecha_inicial.day,28))

print ("Fecha inicial: " + str(fecha_inicial))
print ("Fecha final: " + str(fecha_final))

# A partir de esta línea indica como resolverías el reto.

