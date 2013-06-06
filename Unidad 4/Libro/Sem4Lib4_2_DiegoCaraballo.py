#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 10/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 4.2. Mantenimiento del tarifador:
a) Al nuevo programa que cuenta con llamadas cortas y largas, agregarle los adicionales,
de modo que:
Los montos se escriban como pesos y centavos.
Se informe además cuál fue el total facturado en la corrida.
b) Modificar el programa para que sólo informe cantidad de llamadas cortas, valor to-
tal de llamadas cortas facturadas, cantidad de llamadas largas, valor total de llamadas
largas facturadas, y total facturado. Al llegar a este punto debería ser evidente que es
conveniente separar los cálculos en funciones aparte."""

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
			costo_total_largas = 0
			cont_largas = 0 #contador de llamadas largas
			total_largas = 0 #costo total de las llamadas largas
			con_descuento = descuento (f, segcalc, total)
			centavos = a_centavos(con_descuento)
			print "Duracion: ", segcalc, "segundos. Costo: ",con_descuento, "$."
			print "Duracion: ", segcalc, "segundos. Costo: ", centavos, "centavos."
			cont_largas += 1
			total_largas += con_descuento
			costo_total_largas += con_descuento
		else:
			costo_total_cortas = 0
			cont_cortas = 0 #contador de llamadas cortas
			total_cortas = 0 #costo total de las llamadas cortas
			sin_descuento = sindescuento (f, segcalc)
			centavos = a_centavos (sin_descuento)
			print "Duracion: ", segcalc, "segundos. Costo: ", sin_descuento, "$:"
			print "Duracion: ", segcalc, "segundos. Costo: ", centavos, "centavos."
			cont_cortas += 1
			total_cortas += sin_descuento
			costo_total_cortas += sin_descuento
			
	print "Se hicieron", cont_cortas, "llamada/s cortas y su costo fue de:", total_cortas, "$."
	print "se hicieron", cont_largas, "llamada/s largas y su costo fue de:", total_largas, "$."
	costo_corridas = total_corridas (costo_total_largas, costo_total_cortas)
	print "El costo total de las corridas fue de:", costo_corridas, "$."
			
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
	
def a_centavos (num): #convierte el costo en centavos
	num = num * 100
	return num
	
def total_corridas (total1, total2):
	total = 0
	total = total1 + total2
	return total
		

main()


