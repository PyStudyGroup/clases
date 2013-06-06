#!/usr/bin/python
#!coding: utf-8

inicio_curso = input ("Introduce el año de inicio del curso:")

for z in range(1,4):
    
    name = raw_input ("¿Tu nombre?:>>>  ")
    year_birth = raw_input ("¿Tu año de nacimiento?:>>>  ")
    
    old = int(inicio_curso) - int(year_birth)
    
    print ("Tu nombre es ", name, "Este año cumples",old)
