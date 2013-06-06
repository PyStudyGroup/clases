#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Libro 4.2

# Modiﬁcar el programa tarifador.py para que sólo informe cantidad de 
# llamadas cortas, valor total de llamadas cortas facturadas, cantidad
# de llamadas largas, valor total de llamadas largas facturadas, y total 
# facturado. 

def main():
    
    linea = "-" * 79
    
    dur_llamada = int(raw_input("¿Cuál es la duración máxima de una llamada corta (en segundos)?: "))
    corta = float(raw_input("¿Cuánto cuesta el segundo de la llamada corta?: "))
    larga = float(raw_input("¿Cuánto cuesta el segundo de la llamada larga?: "))
    cantidad = int(raw_input("¿Cuántas comunicaciones hubo?: "))
    print linea, "\n", linea
    
    total_corta = 0
    total_larga = 0
    costo_total = 0
    cortas = 0
    largas = 0    
    
    for x in range(cantidad):
        print "Llamada N°:", x + 1
        hs = int(raw_input("¿Cuántas horas?: "))
        min = int(raw_input("¿Cuántos minutos?: "))
        seg = int(raw_input("¿Cuántos segundos?: "))
        print linea
        segcalc = asegundos(hs, min, seg)
        
        if segcalc < dur_llamada:
            costo = segcalc * corta
            total_corta += costo
            cortas += 1
        else:
            costo = segcalc * larga
            total_larga += costo
            largas += 1
        
        pesos_c, centavos_c = apesycent(total_corta)
        pesos_l, centavos_l = apesycent(total_larga)
        
        costo_total += costo
        
        pesos_t, centavos_t = apesycent(costo_total)

    print linea
    print "Llamadas cortas:", cortas
    print "Costo:", pesos_c, "pesos con", centavos_c, "centavos."
    print linea
    print "Llamadas largas:", largas
    print "Costo:", pesos_l, "pesos con", centavos_l, "centavos."
    print linea
    print "Total recaudado:", pesos_t, "pesos con", centavos_t, "centavos."
    print linea

def asegundos(horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal
        
def apesycent(valor):
    pesos = int(valor // 1)
    centavos = int(round((valor % 1) * 100))
    return pesos, centavos

main()
