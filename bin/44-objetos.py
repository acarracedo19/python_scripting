# Script para mostrar el uso de los objetos

class CuentaBancaria:
	def __init__(self,nombre, balance = 0.0):
		self.log("Cuenta creada")
		self.nombre = nombre
		self.balance = balance

	def ObtenBalance(self):
		self.log("Balance de la cuenta: " + str(self.balance))
		return self.balance

	def PonBalance(self, nuevoBalance):
		self.log("Balance cambio a: " + str(nuevoBalance))
		self.balance= nuevoBalance

	def log(self, mensaje):
		log_transaccion = open("../output/transacciones.txt","a")
		print(mensaje, file = log_transaccion)
		log_transaccion.close()

cuenta = CuentaBancaria("Steve Jobs")
cuenta.PonBalance(15.0)
print(cuenta.ObtenBalance())
