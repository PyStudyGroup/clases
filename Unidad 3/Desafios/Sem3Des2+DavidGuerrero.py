#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/05/2013
@author: DeivGuerrero
'''

def agregaContacto(contactos):
    contactos += "-" * 20 + "\n"
    contactos += "-" * 20 + "\n"
    contactos += input("Dame tu Nombre:") + "\n"
    contactos += input("Dame tu Telefono:") + "\n"
    contactos += input("Dame tu e-mail:") + "\n"
    return main(contactos)


def main(contactos):
    opcion = input("Agregar contacto [si=1 / no=0]:")
    if opcion == 1:
        return agregaContacto(contactos)
    else:
        return "\nMi lista de contactos \n" + contactos

print main("")