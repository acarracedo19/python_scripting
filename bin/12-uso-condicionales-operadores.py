# Script para mostrar el uso de condicionales y operadores

temperatura = -3.5
celsius = True

if ((celsius == True) and temperatura <= 0.0) or ((celsius == False) and temperatura <= 32.0):
    print ("La temperatura " + str(temperatura) + " indica punto de congelación")
else:
    print ("La temperatura " + str(temperatura) + " no indica punto de congelación")

print ("Finalizado")
