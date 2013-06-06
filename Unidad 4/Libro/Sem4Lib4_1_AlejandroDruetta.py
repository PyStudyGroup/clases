#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Libro 4.1

def main():
	""" El usuario ingresa la tarifa por segundo, cuántas
		comunicaciones se realizaron, y la duracion de cada
		comunicación expresada en horas, minutos y segundos. Como
		resultado se informa la duración en segundos de cada
		comunicación y su costo. """
	
	llamCorta = input("¿Cuál es la duración máxima de una llamada corta (en segundos)?: ")
	corta = input("¿Cuánto cuesta el segundo de la llamada corta?: ")
	larga = input("¿Cuánto cuesta el segundo de la llamada larga?: ")
	cantidad = input("¿Cuántas comunicaciones hubo?: ")
	
	costo_total = 0
	
	for x in range(cantidad):
		hs = input("¿Cuántas horas?: ")
		min = input("¿Cuántos minutos?: ")
		seg = input("¿Cuántos segundos?: ")
		segcalc = asegundos(hs, min, seg)
		
		if segcalc > llamCorta:
			costo = segcalc * larga
		else:
			costo = segcalc * corta
		
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
	centavos = round((coste % 1) * 100)
	return centavos

main()
