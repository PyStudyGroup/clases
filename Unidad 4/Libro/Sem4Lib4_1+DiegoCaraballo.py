#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 11/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 4.1. El usuario del tarifador nos pide ahora una modificación, ya que no es lo mismo
	la tarifa por segundo de las llamadas cortas que la tarifa por segundo de las llamadas largas.
	Al inicio del programa se informará la duración máxima de una llamada corta, la tarifa de las
	llamadas cortas y la de las largas. Se deberá facturar con alguno de los dos valores de acuerdo
	a la duración de la comunicación."""

def main():
	
	print "Las llamadas cortas van desde los 0 segundos a 1 hora"
	print "Las llamadas largas son las llamadas mayores a 1 hora"
	print "y tienen un 5 % de descuento en el total"
	

	f = input("¿Cuánto cuesta 1 segundo de comunicacion?: ")
	n = input("¿Cuántas comunicaciones hubo?: ")
	for x in range(n):
		hs = input("¿Cuántas horas?: ")
		min = input("¿Cuántos minutos?: ")
		seg = input("¿Cuántos segundos?: ")
		segcalc = asegundos(hs, min, seg)
		total = segcalc * f
		if hs > 0:
			con_descuento = descuento (f, segcalc, total)
			print "Duracion: ", segcalc, "segundos. Costo: ",con_descuento, "$."
		else:
			sin_descuento = sindescuento (f, segcalc)
			print "Duracion: ", segcalc, "segundos. Costo: ", sin_descuento, "$:"
			
def asegundos (horas, minutos, segundos):
	segsal = 3600 * horas + 60 * minutos + segundos
	return segsal
	
def descuento (x, segundos, calc): #Calcula el costo con el descuento del 5 %
	descuen = 0
	descuen = float (descuen)
	x = float (x)
	descuen = (x * 5) / 100
	descuen = descuen * segundos
	costo = calc - descuen
	return costo
	
def sindescuento (x, segundos): #Calcula el costo sin descuento

	total = x * segundos
	return total

main()
