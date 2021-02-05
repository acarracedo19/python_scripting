# Script para mostrar el uso de las funciones

def habito_soda(soda_de_preferencia,costo_por_soda,calorias_por_soda,sodas_por_semana):
	dinero_gastado = costo_por_soda * sodas_por_semana
	calorias_consumidas = calorias_por_soda * sodas_por_semana

	texto = "Estas gastando $" + str(dinero_gastado) + " en \""
	texto += soda_de_preferencia + "\" a la semana.\n"
	texto += "Lo que equivale a " + str(calorias_consumidas) + " calorias !!!"

	return texto

print(habito_soda("Sprite",1.75,140,9))
