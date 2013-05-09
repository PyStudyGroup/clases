#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Semana 3 - Desafío 1

# Escribe una función es_primo que tome un número x como entrada y 
# devuelva el booleano Verdadero si x es primo y Falso si no lo es.

def main():

	numero = input("Ingrese un número natural >= 2: ")
	
	print "¿Es un número primo?", es_primo(numero)

def es_primo(entero):
	
	primo = 1
	
	for x in range(2, entero):
		modulo = entero % x
		
		# Si en algún momento modulo es 0, la multiplicación dará 0, y 
		# 'primo' será False. De lo contrario, será True.
		
		primo *= modulo				
	
	return bool(primo)

main()
