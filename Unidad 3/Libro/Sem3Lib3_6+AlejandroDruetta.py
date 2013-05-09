#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 3 - Libro 3.6

# Corregir el programa tarifador.py para que:
# Imprima el costo en pesos y centavos, en lugar de un número decimal.
# Informe además cuál fue el total facturado en la corrida.

def main():
	""" El usuario ingresa la tarifa por segundo, cuántas
		comunicaciones se realizaron, y la duracion de cada
		comunicación expresada en horas, minutos y segundos. Como
		resultado se informa la duración en segundos de cada
		comunicación y su costo. """
	
	f = input("¿Cuánto cuesta 1 segundo de comunicacion?: ")
	n = input("¿Cuántas comunicaciones hubo?: ")
	
	costo_total = 0
	
	for x in range(n):
		hs = input("¿Cuántas horas?: ")
		min = input("¿Cuántos minutos?: ")
		seg = input("¿Cuántos segundos?: ")
		segcalc = asegundos(hs, min, seg)
		costo = segcalc * f
		costo_total += costo
		
		print "Duracion: ", segcalc, "segundos. Costo: ", int(apesos(costo)), "$ y", int(acentavos(costo)), "centavos."

	print "El costo total es: $", costo_total

def asegundos(horas, minutos, segundos):
	segsal = 3600 * horas + 60 * minutos + segundos
	return segsal
		
def apesos(coste):
	pesos = coste // 1
	return pesos
	
def acentavos(coste):
	centavos = round((coste % 1) * 100)		# Me hubiera gustado resolverlo sin usar round...
	return centavos

main()
