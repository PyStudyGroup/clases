#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.1 del Libro
Autores:    Carlos Llamacho y Alejandro Druetta
Fecha:      20/05/13
"""

def main():
    
    # Menú de procedimientos:
             
    print "Procedimientos:\n"
    print "1. Ciclo deﬁnido."
    print "2. Ciclo interactivo."
    print "3. Ciclo con centinela."
    print "4. Ciclo 'inﬁnito' que se rompe.\n"
    
    opcion = int(raw_input("Elija un procedimiento (1-4): "))
    
    while True:
                
        if opcion == 1:
            ciclo_definido()
            break
        elif opcion == 2:
            ciclo_interactivo()
            break
        elif opcion == 3:
            ciclo_centinela()
            break
        elif opcion == 4:
            break
        else:
            print
            opcion = int(raw_input("Opción incorrecta, intente nuevamente: "))

def ciclo_definido():
    
    linea = "-" * 79
    
    print
    tarifa = float(raw_input("¿Cuánto cuesta un segundo de comunicación?: "))
    llamadas = int(raw_input("¿Cuántas llamadas se realizaron?: "))
    print
    
    for llamada in range(llamadas):
        
        print "Llamada %d:\n" % (llamada + 1)
        hs = int(raw_input("¿Cuántas horas?: "))
        ms = int(raw_input("¿Cuántos minutos?: " ))
        ss = int(raw_input("¿Cuántos segundos?: "))
        print
        
        segundos = asegundos(hs, ms, ss)
        coste = segundos * tarifa
        
        print linea
        print "La llamada duró %d segundos y costó %4.2f euros." % (segundos, coste)
        print linea, "\n"
        
def ciclo_interactivo():
    """Facturar el uso de un telefono usando un ciclo interactivo."""
    
    cant_llamadas = 1
    llamadas = True
    
    while llamadas:
        print "-"*50
        horas = int(raw_input("Horas de la llamada #{0}? ".format(cant_llamadas)))
        minutos = int(raw_input("Minutos de la llamada #{0}? ".format(cant_llamadas)))
        segundos = int(raw_input("Segundos de la llamada #{0}? ".format(cant_llamadas)))
        print "*"*20
        print "Su costo de llamada es de ${0}.".format(calcular_tarifa(horas, minutos, segundos))    
        print "-"*50
        cant_llamadas += 1
        
        continuar = str(raw_input("Tiene más llamadas que facturar? (Si/No): "))
        
        if continuar == "No":
            llamadas = False

def ciclo_centinela():
    
    linea = "-" * 79
    llamada = 1
    centinela = ""
    
    print
    tarifa = float(raw_input("¿Cuánto cuesta un segundo de comunicación?: "))
    print
    
    while centinela != "s":
        
        print "Llamada %d:\n" % llamada
        hs = int(raw_input("¿Cuántas horas?: "))
        ms = int(raw_input("¿Cuántos minutos?: " ))
        ss = int(raw_input("¿Cuántos segundos?: "))
        print
        
        segundos = asegundos(hs, ms, ss)
        coste = segundos * tarifa
        
        print linea
        print "La llamada duró %d segundos y costó %4.2f euros." % (segundos, coste)
        print linea, "\n"
        
        centinela = raw_input("Presione 'Enter' para continuar, 's' para salir: ")
        centinela = centinela.lower()
        print
        
        llamada += 1

def calcular_tarifa(horas, minutos, segundos):
    """Calcula la tarifa segun la duración de la llamada, que se le pasa.
    Los costos son fijos. $2.00 el minuto. Segundos se redondean, mas de la mitad se cuenta.
    Menos no aplica costos."""
    
    costo = 0    
    
    horas = horas * 60
    costo = costo + (horas * 2)
    costo = costo + (minutos * 2)
    if segundos >= 30:
        segundos = 1
    else:
        segundos = 0
    costo = costo + round((segundos * 2))
    
    return costo
        
def asegundos(horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()
