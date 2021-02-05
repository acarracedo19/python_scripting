# Script para explicar el uso del auto incremento de variables

# Define variables
Variable_1 = 5
print ("Valor inicial de \"Variable_1\": " + str(Variable_1))
Variable_1 = Variable_1 + 3
print ("Ahora el valor \"Variable_1\" es: " + str(Variable_1))
Variable_1 = Variable_1 // 2
print ("Ahora el valor de \"Variable_1\" es: " + str(Variable_1))
Variable_1 = Variable_1 ** 2
print ("Valor final de \"Variable_1\": " + str(Variable_1))

Variable_2 = 5
print ("\n\nValor inicial de \"Variable_2\": " + str(Variable_2))
Variable_2 += 7
print ("Ahora el valor \"Variable_2\" es: " + str(Variable_2))
Variable_2 /= 3
print ("Ahora el valor de \"Variable_2\" es: " + str(Variable_2))
Variable_2 **= 3
print ("Valor final de \"Variable_2\": " + str(Variable_2))
