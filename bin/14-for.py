# Script para mostrar el uso de for

sum = 0
factorial = 1

for i in range (1,11):
	numero_siguiente = int(input("Ingresa un número #" + str(i) + ": "))
	sum += numero_siguiente

print("El promedio es: " + str(sum/10))

print("\n")
numero_factorial = int(input("Ingresa un número para calcular su factorial: "))

for i in range(1,numero_factorial+1):
	factorial *= i
print("El número factorial de " + str(numero_factorial) + " es: " + str(factorial))
