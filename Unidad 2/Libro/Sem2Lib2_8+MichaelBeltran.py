#!/usr/bin/python
#-*- encoding: utf-8 -*-

def saludo():
    amigos=input("Cuantos amigos quieres saludar: ")
    for i in range(0,amigos):
        nombre=raw_input("Dime el nombre: ")
        print "hola: "+nombre


saludo()
