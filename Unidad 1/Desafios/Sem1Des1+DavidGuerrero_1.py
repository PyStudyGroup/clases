#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Solicitamos al usuario  el año
anioActual = raw_input("Año Actual:")

#Verificamos que la cadena este compuesta de dígitos
if anioActual.isdigit():
    #convertimos de string a int (de cadena a numero entero)
    anioActual = int(anioActual)
    
    #Creamos un ciclo que se ejecute 3 veces
    for i in range(3):
        #Solicitamos un nombre
        nom = raw_input("Nombre:")
    
        #Solicitamos año de nacimiento
        anioNac = raw_input("Año de Nacimiento:")
        
        #verificamos que sean digitos
        if anioNac.isdigit():
            """Obtenemos la edad, recordemos que anioNac es una cadena
                por lo tanto lo convertimos a entero
            """
            edad =  anioActual - int(anioNac)
            
            """Imprimimos el resultado formateando la salida el %s será
                reemplazado por lo que la variable nom contenga, de la misma
                forma el %d (que hace referencia a digitos) será reemplazada
                con el valor de la variable edad.
            """
            print "%s en este año cumpliras %d\n" % (nom, edad)
        else:
            #En dado caso que la variable anioNac no sea una cadena de digitos
            print "Debes introducir un año válido (dígitos)"
else:
    #En dado caso que la variable anioActual no sea una cadena de digitos
    print "Debes introducir un año válido (dígitos)"