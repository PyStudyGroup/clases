#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Ejercicio 3

# Hacer un método que recibe un numero positivo, y devuelve la suma de 
# cada digito.

def main():
	
	entrada = input("Ingrese un número positivo: ")
	print "La suma de sus dígitos es igual a:", suma_digitos(entrada)
	
def suma_digitos(numero):
	
	suma = 0
	
	for x in str(numero):
		suma += int(x)
	return suma
		
main()


