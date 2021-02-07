# Script para mostrar el uso de los objetos

class Servidor:
	def __init__(self,vcpu,ram,nombre,sistema_operativo,almacenamiento):
		self.vcpu = vcpu
		self.ram = ram
		self.nombre = nombre
		self.sistema_operativo = sistema_operativo
		self.almacenamiento = almacenamiento

servidor_1 = Servidor(2,"4 GB","AWS-SVR-1","Windows","20 GB")
servidor_2 = Servidor(4,"8 GB","AWS-SVR-2","Linux","30 GB")

print(servidor_1.nombre)
print(servidor_1.sistema_operativo)
print(servidor_1.vcpu)

print("\n-----\n")

print(servidor_2.nombre)
print(servidor_2.ram)
print(servidor_2.almacenamiento)
