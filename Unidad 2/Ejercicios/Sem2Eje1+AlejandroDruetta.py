#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 28/04/13
# Python 2.7.4
# Semana 2 - Ejercicio 1
# Nivel de dificultad: Media

##----------------------------Problema--------------------------------##
## Escribir un programa que calcule el costo total de una compra de   ##
## libros. Primero pregunta la cantidad de libros y la taza de        ##
## impuestos. Luego pregunta el título y el precio de cada libro.     ##
## Finalmente, imprime el número de libros, la suma del valor de los  ##
## libros, el valor de los impuestos y el total a pagar.              ##
##--------------------------------------------------------------------##

def main():
	""" Calcula el costo total y discriminado de una compra. """
	
	# Ingresar datos cantidad libros e impuestos.
	libros = input("¿Cuántos libros lleva?: ")
	tasa = input("¿% de impuestos?: ")
	
	# Contador inicializado.
	tot_precio = 0	
	# Contador inicializado.
	tot_impuesto = 0	
	
	# Función calcula el valor del impuesto.
	def calc_impuesto(p, t):
		""" Recibe precio y taza como argumentos y retorna el valor
			del impuesto
		"""
		impuesto = (p / 100.0) * t
		return impuesto

	# Tantas iteraciones como libros.
	for x in range(libros):
		# Ingresa cadena de caracteres.	
		titulo = raw_input("¿Título del libro?: ")
		# Ingresa valor numérico.
		precio = input("¿Cuánto vale?: ")
		# Acumula el precio.
		tot_precio += precio
		# Acumula los impuestos.
		tot_impuesto += calc_impuesto(precio, tasa)	
	
	# Impresión de resultados.
	print "*" * 25
	print "Cantidad: ", libros
	print "Precio: $", tot_precio
	print "Impuestos: $", tot_impuesto
	print "Total a pagar: $", tot_precio + tot_impuesto
	print "*" * 25
	
main ()
