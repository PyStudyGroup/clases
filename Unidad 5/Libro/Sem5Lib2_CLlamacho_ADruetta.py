#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.2 del Libro
Autores:    Carlos Llamacho y Alejandro Druetta
Fecha:      21/05/13
"""
#Esta funcion termina el flujo del programa.
from sys import exit

def main():
    
    # Menú de procedimientos:
             
    print "Procedimientos:\n"
    print "1. Ciclo deﬁnido."
    print "2. Ciclo interactivo."
    print "3. Ciclo con centinela."
    print "4. Ciclo 'inﬁnito' que se rompe."
    print "5. Salir.\n"

    opcion = raw_input("Elija un procedimiento (1-5): ")
    print

    while True:
        
        if opcion in "12345":
            break
        else:
            opcion = raw_input("Opción incorrecta, intente nuevamente: ")
    
    if opcion == "5":
        exit()
    
    print "-" * 79
    tarifa = float(raw_input("¿Cuánto cuesta un segundo de comunicación? (euros): "))
    
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
    
    total_facturado = 0
    cant_llamadas = int(raw_input("¿Cuántas llamadas se realizaron?: "))
    print "-" * 79
    
    for llamada in range(cant_llamadas):
        total_facturado += calculo(llamada, tarifa)
    
    informe(cant_llamadas, total_facturado)
    main()
        
def ciclo_interactivo(tarifa):
    """Facturar el uso de un telefono usando un ciclo interactivo."""
    
    cant_llamadas = 0
    llamadas = True
    total_facturado = 0
    
    while llamadas:
        
        total_facturado += calculo(cant_llamadas, tarifa)
        cant_llamadas += 1
        continuar = raw_input("Tiene más llamadas que facturar? (Si/No): ")
        continuar = continuar.lower()
        if continuar == "no":
            llamadas = False
    
    informe(cant_llamadas, total_facturado)
    main()

def ciclo_centinela(tarifa):
    """Facturar el uso de un telefono usando un ciclo con centinela."""
    
    cant_llamadas = 0
    centinela = ""
    total_facturado = 0
        
    while centinela != "s":
        
        total_facturado += calculo(cant_llamadas, tarifa)
        
        centinela = raw_input("Presione 'Enter' para continuar, 'S' para salir: ")
        centinela = centinela.lower()
        
        cant_llamadas += 1
        
    informe(cant_llamadas, total_facturado)
    main()
        
    
def ciclo_infinito(tarifa):
    """Facturar el uso de un telefono usando un ciclo infinito que se interrumpe."""
    
    cant_llamadas = 0
    total_facturado = 0
    while True:
        
        total_facturado += calculo(cant_llamadas, tarifa)
        
        continuar = raw_input("Tiene más llamadas que facturar? (Si/No): ")
        continuar = continuar.lower()
        cant_llamadas += 1
        if continuar == "no":
            break
    
    informe(cant_llamadas, total_facturado)
    main()

def calculo(cant_llamadas, tarifa):
    """Calcula la tarifa e imprime el resultado."""
    
    print ">>> Llamada %d <<<" % (cant_llamadas + 1)
    hs = int(raw_input("¿Cuántas horas?: "))
    ms = int(raw_input("¿Cuántos minutos?: " ))
    ss = int(raw_input("¿Cuántos segundos?: "))
    
    segundos = asegundos(hs, ms, ss)
    coste = segundos * tarifa
    
    print "-" * 79
    print "La llamada duró {0} segundos y costó {1} euros.".format(segundos, coste)  
    print "-" * 79

    return coste
    
def informe(cant_llamadas, total_facturado):
    
    # Mensaje con marco:
    
    mensaje = " Usted ha realizado un total de {0} llamadas con un valor de {1} euros. ".format(cant_llamadas, total_facturado)
    espacios = 79 - len(mensaje)
    if espacios % 2 == 0:
        espacio_ini = espacios / 2
        espacio_fin = espacio_ini
    else:
        espacio_ini = espacios // 2
        espacio_fin = espacios // 2 + espacios % 2
    
    print
    print "*" * 79
    print ("*" * espacio_ini) + mensaje + ("*" * espacio_fin)
    print "*" * 79
    
    # Mensaje simple:
    # print "Usted ha realizado un total de {0} llamadas con un valor de {1} euros.".format(cant_llamadas, total_facturado)
        
def asegundos(horas, minutos, segundos):
    """Convierte a segundos el valor ingresado en horas, minutos y segundos."""
    
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()
