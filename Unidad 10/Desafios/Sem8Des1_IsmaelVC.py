#!/usr/bin/env python3

from subprocess import call
import sys
from textwrap import dedent as dd
from time import sleep

def validar_cadena(cadena):
    try:
        float(cadena)
    except ValueError:
        print("ERROR! La cadena: '{cadena}', NO es una expresion valida, para numeros flotantes.".format(**vars()))
    else:
        print("La cadena: '{cadena}', es una expresion valida, para numeros flotantes.".format(**vars()))
  

def main():
    prompt = chr(10144)
    while True:
        call('clear')
        cadena_in = input(dd('''\
                             Escriba una expresion para numeros flotantes, 
                             su validez sera evaluada: (S/SALIR, para finalizar)
                             {prompt} '''.format(**vars())))
        if cadena_in.lower() in ['s', 'salir']:
            sys.exit()
        else:
            validar_cadena(cadena_in)
            sleep(4)
    
  
if __name__ == '__main__':
    main()

