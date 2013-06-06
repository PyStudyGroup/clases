# -*- coding: utf-8 -*-

def saludo():
    nombre = input("Nombre:")
    print "Hola ", nombre

namigos = input("¿A cuantos amigos quieres saludar?")

for i in range(namigos):
    saludo()