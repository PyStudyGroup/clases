#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Semana 5 - Ejercicio 5.1 del Libro
Autores:    Carlos Llamacho y Alejandro Druetta
Fecha:      20/05/13
"""

def main():
    
    # Menú de procedimientos:
            
    print "Procedimientos: "
    print "1. Ciclo deﬁnido."
    print "2. Ciclo interactivo."
    print "3. Ciclo con centinela."
    print "4. Ciclo 'inﬁnito' que se rompe."
    
    opcion = int(raw_input("Elija un procedimiento (1-4): "))
    
    while True:
                
        if opcion == 1:
            break
        elif opcion == 2:
            ciclo_interactivo()
            break
        elif opcion == 3:
            break
        elif opcion == 4:
            break
        else:
            opcion = int(raw_input("Opción incorrecta, intente nuevamente: "))
            
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
    
        
main()
