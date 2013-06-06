#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 11/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Escriba un programa que pida dos números enteros y que calcule su división,
 escribiendo si la división es exacta o no."""
 
def main():
	 print "Divisor de numeros"
	 dividendo = input ("Escriba el dividendo: ")
	 divisor = input ("Escriba el divisor: ")
	 if divisor == 0:
		 print "No se puede dividir por 0"
		 main()
	 else:
		resultado = divisor_de_numeros (dividendo, divisor)
		resto = calcular_resto (dividendo, divisor)
		if resto == 0:
			print "La division es exacta. Cociente:", resultado
		else:
			print "La division no es exacta. Cociente:", resultado, "Resto: ", resto
	 
def divisor_de_numeros(x, n):
	resul = x / n
	return resul
	
	
def calcular_resto (x, n):
	rest = x % n
	return rest


main()
