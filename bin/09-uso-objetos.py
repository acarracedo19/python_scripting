# Script para mostrar el uso de los objetos

from datetime import date, datetime

# Define variables
fecha = date.today()
fecha_hora = datetime.now()

print("La fecha es: " + str(fecha))
print("El año es: " + str(fecha.year))
print("El mes es: " + str(fecha.month))
print("El día es: " + str(fecha.day) + "\n")

print("La fecha es: " + str(fecha_hora))
print("El día de la semana es: " + fecha_hora.strftime("%A"))
print("La semana del año es: " + fecha_hora.strftime("%w"))
print("El mes del año es: " + fecha_hora.strftime("%B"))
print("El día del mes es: " + fecha_hora.strftime("%d"))
print("La hora es: " + fecha_hora.strftime("%H"))
print("El minuto es: " + fecha_hora.strftime("%M"))
print("Los segundos son: " + fecha_hora.strftime("%S"))
print("Los microsegundos son: " + fecha_hora.strftime("%f"))
