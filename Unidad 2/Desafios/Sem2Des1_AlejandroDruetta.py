#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @version: Python 2.7.4
# @date: 03/05/13
# Grupo de Estudio Python

def main():
	''' Convierte un número binario a entero. '''
		
	bin = raw_input("Ingrese un número binario: ")
	
	# Necesitamos multiplicar cada bit por 2 elevado a la potencia igual
	# a su posición -1 de atrás para adelante. Entonces vamos a comenzar
	# con el equivalente a su extensión -1.
	
	y = len(bin) - 1
	
	entero = 0
	
	# Ciclo donde x toma el valor de cada elemento de 'bin'.
	
	for x in bin:
		
		# 'Entero' acumula el cálculo de conversión de binario a entero.
		
		entero += int(x) * 2 ** y
		
		# 'y' retrocede una posición.
		
		y -= 1
	
	# Imprime en pantalla el resultado.	
	
	print "La representación decimal del binario", bin, "es", entero

main()
