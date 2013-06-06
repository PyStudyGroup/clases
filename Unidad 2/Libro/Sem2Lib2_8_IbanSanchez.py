#!/usr/bin/python
#!coding: utf-8
#Python 2.7
#Ibán Sánchez
def main():
    s = int(raw_input("¿A cuantos amigos quieres saludar?: "))      #Definimos la variable "s" para obtener el numero de nombres a saludar.
    for z in range(0, s):                                           #Aquí para la variable z marcamos un rango de 0 a s, la variable anterior
        k = raw_input("Introduce un nombre: ")                      #Creamos la variable k, que es donde introduciremos los nombres
        print "hola", k, ":))"                                      #Esta línea hace que imprima el saludo a cada nombre introducido, el ciclo entero se va repitiendo para cada nombre.
main()
