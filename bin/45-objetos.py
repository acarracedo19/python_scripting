# Script para mostrar el uso de los objetos

class CuentaBancaria:
	def __init__(self,nombre, balance = 0.0):
		self.log("Cuenta creada para: " + nombre)
		self.nombre = nombre
		self.balance = balance

	def ObtenBalance(self):
		self.log("Balance de la cuenta: " + str(self.balance))
		return self.balance

	def Deposito(self, cantidad):
		self.log("+" + str(cantidad) + ": " + str(self.balance))
		self.balance += cantidad

	def Retiro(self, cantidad):
		self.log("-" + str(cantidad) + ": " + str(self.balance))
		self.balance -= cantidad

	def log(self, mensaje):
		log_transaccion = open("../output/transacciones.txt","a")
		print(mensaje, file = log_transaccion)
		log_transaccion.close()

cuenta = CuentaBancaria("Jeff Bezos")
cuenta.Deposito(25.0)
print(cuenta.ObtenBalance())
cuenta.Retiro(10.0)
print(cuenta.ObtenBalance())
