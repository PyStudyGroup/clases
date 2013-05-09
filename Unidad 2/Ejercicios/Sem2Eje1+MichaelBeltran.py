#!/usr/bin/python
#-*- encoding: utf-8 -*-
def libros():
    r=input("cantidad de libros: ")
    i=input("taza de impuestos: ")
    t=0#se inicializa la variable
    r+=1
    for j in range(1,r):
        print j,
        raw_input("Titulo de el Libro: ")
        v=input("precio del libro: ")
        t+=v#el total de los libros
    j+=1#cantidad de libros
    np=((t//100)*i)+t#neto a pagar 
    i=(t//100)*i#impuestos 
    print "*"*30
    print "*numero de libros:",j
    print "*total:",t
    print "*total de impuestos:",i
    print "*neto a pagar",np
    print "*"*30

libros()
