#!/usr/bin/env python3

import os
import re
import subprocess
import sys

from textwrap import dedent as dd


ESPECIFICACION = '''
Literales de puntos flotantes.

Los literales de puntos flotantes son descritos por las siguientes definiciones lexicas:

numeroflotante    ::=  puntoflotante | exponenteflotante
puntoflotante     ::=  [parteint] fraccion | parteint "."
exponenteflotante ::=  (parteint | puntoflotante ) exponente
parteint          ::=  digito+
fraccion          ::=  "." digito+
exponente         ::=  ("e" | "E") ["+" | "-"] digito+

Note que las partes integrales y exponentes siempre son interpretadas usando base 10.
Por ejemplo, 077e010 es legal, y denota al mismo numero que 77e10. El rango de literales
de punto flotante permitido depende de la implementacion. Algunos ejemplos de literales
de puntos flotantes:

3.14    10.    .001    1e100    3.14e-10    0e0

Note que los literales numericos no incluyen un signo; la frase -1 es en realidad una
expresion compuesta por el operador unario - y el literal 1.
'''

regex = r'''
        ^          # Coincide con el inicio de la cadena,
        [\s]*      # seguido por 0 o mas espacios,
        ([+-]?)    # seguido por 0 o 1 coincidencia del signo de positivo o negativo,
        ([\d]*)    # seguido por 0 o mas numeros (parte entera),
        ([.]?)     # seguido por 0 o 1 punto,
        ([\d]*)    # seguido por 0 o mas numeros (parte flotante),
        ([e]?)     # seguido por 0 o 1 coincidencia de exponente,
        ([-]?)     # seguido por 0 o 1 signo negativo del exponente,
        ([\d]*)    # seguido por 0 o mas numeros (parte exponente),
        [\s]*      # seguido por 0 o mas espacios,
        $          # seguido por el final de la cadena.
        '''

patron = re.compile(regex, re.I|re.X)
error = '''"ERROR! La cadena: '{cadena}', NO es una expresion valida, para numeros flotantes.".format_map(vars())'''

def clear():
    if os.name == 'posix':
        subprocess.call('clear')
    else:
        os.system('cls')


def primera_validacion(cadena):
    if cadena.lower() in ['inf', 'infinity', 'nan']:
        return cadena
    coincidencia = patron.search(cadena)
    if coincidencia:
        _coincidencia = coincidencia.groups()
        print(dd('''
                 coincidencia: {_coincidencia}

                 signo     : {_coincidencia[0]}
                 entero    : {_coincidencia[1]}
                 punto     : {_coincidencia[2]}
                 decimal   : {_coincidencia[3]}
                 marca_exp : {_coincidencia[4]}
                 signo_exp : {_coincidencia[5]}
                 exponente : {_coincidencia[6]}
                 '''.format_map(vars())))
        return coincidencia.group()
    else:
        print(eval(error))


def segunda_validacion(cadena):
    try:
        float(cadena)
    except ValueError:
        print("\nHumanProcessorError: Falso positivo en la primera validacion: '{cadena}'.\n".format_map(vars()))
        print(eval(error))
    else:
        print("\nLa cadena: '{cadena}', es una expresion valida, para numeros flotantes.".format_map(vars()))


def main():
    # prompt = chr(10144)   # cmd.exe es tan patetico...
    while True:
        clear()
        cadena_in = input(dd('''\
                             Escriba una expresion para numeros flotantes,
                             su validez sera evaluada: (S/SALIR, para finalizar)
                             => '''.format_map(vars())))
        if cadena_in.lower() in ['s', 'salir']:
            sys.exit()
        else:
            prueba = primera_validacion(cadena_in)
            if prueba:
                segunda_validacion(prueba)
            print('\nPresione ENTER para continuar.')
            input()


if __name__ == '__main__':
    main()
