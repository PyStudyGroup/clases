#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.1 del Libro
Autores:    Carlos Llamacho y Alejandro Druetta
Fecha:      20/05/13
"""

def main():
    
    # Menú de procedimientos:
             
    print "Procedimientos:"
    print "1. Ciclo deﬁnido."
    print "2. Ciclo interactivo."
    print "3. Ciclo con centinela."
    print "4. Ciclo 'inﬁnito' que se rompe."

    opcion = raw_input("Elija un procedimiento (1-4): ")

    while True:
        
        if opcion in "1234":
            break
        else:
            opcion = raw_input("Opción incorrecta, intente nuevamente: ")
    
    tarifa = float(raw_input("¿Cuánto cuesta un segundo de comunicación?: "))
    
    if opcion == "1":
        ciclo_definido(tarifa)
    elif opcion == "2":
        ciclo_interactivo(tarifa)
    elif opcion == "3":
        ciclo_centinela(tarifa)
    elif opcion == "4":
        ciclo_infinito(tarifa)
            
def ciclo_definido(tarifa):
    """Facturar el uso de un telefono usando un ciclo definido."""
    
    llamadas = int(raw_input("¿Cuántas llamadas se realizaron?: "))
    
    for llamada in range(llamadas):
        calculo(llamada, tarifa)
        
def ciclo_interactivo(tarifa):
    """Facturar el uso de un telefono usando un ciclo interactivo."""
    
    cant_llamadas = 0
    llamadas = True
    
    while llamadas:
        
        calculo(cant_llamadas, tarifa)
        cant_llamadas += 1
        
        continuar = str(raw_input("Tiene más llamadas que facturar? (Si/No): "))
        
        if continuar == "No":
            llamadas = False

def ciclo_centinela(tarifa):
    """Facturar el uso de un telefono usando un ciclo con centinela."""
    
    llamada = 1
    centinela = ""
        
    while centinela != "s":
        
        calculo(llamada, tarifa)
        
        centinela = raw_input("Presione 'Enter' para continuar, 's' para salir: ")
        centinela = centinela.lower()
        
        llamada += 1

def calculo(llamada, tarifa):
    """Calcula la tarifa e imprime el resultado."""
    
    print "Llamada %d:" % (llamada + 1)
    hs = int(raw_input("¿Cuántas horas?: "))
    ms = int(raw_input("¿Cuántos minutos?: " ))
    ss = int(raw_input("¿Cuántos segundos?: "))
    
    segundos = asegundos(hs, ms, ss)
    coste = segundos * tarifa
    
    print "La llamada duró %d segundos y costó %4.2f euros." % (segundos, coste)        
        
def asegundos(horas, minutos, segundos):
    """Convierte a segundos el valor ingresado en horas, minutos y segundos."""
    
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()
