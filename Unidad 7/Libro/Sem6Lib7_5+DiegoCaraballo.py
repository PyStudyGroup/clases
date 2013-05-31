#-*- coding: UTF-8 -*-

"""Ejercicio 7.5. Escribir una función diaSiguienteE que dada una 
fecha expresada como la terna (Día, Mes, Año) (donde Día, Mes y Año 
son números enteros) calcule el día siguiente al dado, en el mismo 
formato."""

def main():
	d = input ("Ingrese un dia del mes: ")
	m = input ("Ingrese un mes (1 al 12): ")
	a = input ("Ingrese un ano: ")
	
	dia_siguiente = diaSiguiente (d, m, a)
	print dia_siguiente

def diaSiguiente(dia, mes, ano):
	de31 = (1, 3, 5, 7, 8, 10, 12)
	de30 = (4, 6, 9, 11)
	de28 = (2, )
	
	
	if (mes == 12) and (dia == 31):
		return (dia - 30), de31[0], (ano + 1)
	elif mes in de31 and dia == 31:
		return (dia - 30), (mes + 1), ano
	elif mes in de30 and dia == 30:
		return (dia - 29), (mes + 1), ano
	elif mes in de28 and dia == 28:
		return (dia - 27), (mes + 1), ano
	else:
		return (dia + 1), mes, ano
	
	
main()
