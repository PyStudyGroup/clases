#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 04/05/2013
@author: DeivGuerrero
'''


def imprimirTabla(numero, inicio, final):
    """Imprime la tabla de multiplicar del
    <numero> recibido en un rango de <inicio> a
    <fin>, no retorna ningun valor."""
    for n in range(inicio, final+1):
        print str(numero) + " x " + str(n) + "=" + str(numero*n)


def main():
    """Funcion principal del módulo"""
    NTabla = input("¿Hasta que Tabla debemos imprimir?:")
    ITabla = input("¿En donde debe Iniciar la tabla?:")
    FTabla = input("¿En donde debe Terminar la tabla?:")
    
    for t in range(1, NTabla+1):
        imprimirTabla(t, ITabla, FTabla)
        print "\n"

main()