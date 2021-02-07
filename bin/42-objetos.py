# Script para mostrar el uso de los objetos

class Servidor:
	def __init__(self):
		self.vcpu = 0
		self.ram = ""
		self.nombre = ""
		self.sistema_operativo = ""
		self.almacenamiento = ""

servidor_1 = Servidor()
servidor_1.vcpu = 2
servidor_1.ram = "4 GB"
servidor_1.nombre = "AWS-SVR-1"
servidor_1.sistema_operativo = "Windows"
servidor_1.almacenamiento = "20 GB"

servidor_2 = Servidor()
servidor_2.vcpu = 4
servidor_2.ram = "8 GB"
servidor_2.nombre = "AWS-SVR-2"
servidor_2.sistema_operativo = "Linux"
servidor_2.almacenamiento = "30 GB"

print(servidor_1.nombre)
print(servidor_1.vcpu)
print(servidor_1.sistema_operativo)

print("\n-----\n")

print(servidor_2.nombre)
print(servidor_2.ram)
print(servidor_2.almacenamiento)
