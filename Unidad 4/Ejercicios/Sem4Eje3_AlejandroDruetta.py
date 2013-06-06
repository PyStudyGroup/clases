#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Alejandro Druetta
# @date: 04/05/13
# @version: python 2.7.4
# Grupo Estudio Python

# Unidad 4 - Ejercicio 3

# Escriba un programa que pida el año actual y un año cualquiera y que 
# escriba cuántos años han pasado desde ese año o cuántos años faltan 
# para llegar a ese año.

def main():
    
    print "Comparador de años"
    year_act = int(raw_input("¿En qué año estamos?: "))
    year = int(raw_input("Escriba un año cualquiera: "))
    
    dif = year_act - year
    
    if dif == 0:
        print "¡Son el mismo año!"
    elif dif > 1:
        print "Desde el año", year, "han pasado", dif, "años."
    elif dif == 1:
        print "Desde el año", year, "ha pasado", dif, "año."
    elif dif == -1:
        dif *= -1
        print "Para llegar al año", year, "falta", dif, "año."
    else:
        dif *= -1
        print "Para llegar al año", year, "faltan", dif, "años."
    
main()
