#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Programa que procesa el codigo Python ingresado por un usuario
y verifica que la indentacion sea concistente. (De momento
unicamente acepta < TAB >s para la indentacion.)
'''

def obtener_input():
    '''
    codigo ingresado -> dict(num_linea: linea)

    Registra el numero de linea y las lineas mismas del codigo
    ingresdo por el usuario y las retorna en un diccionario.
    '''

    linea_nro = 1
    linea_dic = {}

    print "\nIngrese el código (digite 'Salir' para terminar),\nusar TABs en lugar de espacios para indentar:\n"

    while True:

        linea = raw_input("[%d] " % linea_nro)

        # Transforma cadena vacía en espacio en blanco para después poder leer el primer elemento de la cadena.
        if linea == "":
            linea = " "

        # Transforma cualquier línea sólo de tabulaciones en espacio en blanco, para evitar errores de chequeo.
        for i in linea:
            distintos = 0
            if i != "\t":
                distintos += 1
        if distintos == 0:
            linea = " "

        # Sale del ciclo de ingreso de código.
        if linea.lower() == "salir":
            return linea_dic
        else:
            # Crea el diccionario con clave igual a linea_nro y valor igual al código.
            linea_dic[linea_nro] = [linea]
            linea_nro += 1

def calcular_indent(linea_dic):
    '''
    dict(num_linea: linea) -> dict(num_linea: [indentacion, linea])

    Usa un diccionario, con el numero de linea, y la linea misma por cada
    linea del codigo, retorna el diccionario con el nivel de indentacion
    añadido a cada linea.
    '''

    print '\nLINEA\tINDENT\tCONTENIDO'

    for i in range(len(linea_dic)):

        i += 1
        indentacion = 0

        for caracter in linea_dic[i][0]:

            if caracter == "\t":
                indentacion += 1
            '''
            elif caracter ==' ':   # Intento hacer que tambien acepte espacios.
                indent_lst = []    # pero no podre seguir por hoy. <Ismael-VC>
                indent_lst.append(caracter)
            elif caracter !== ' ' of caracter !== '\t':
                break
            '''

        # Inserta el valor de la indentación en la lista antes del código.
        linea_dic[i].insert(0, indentacion)

        print "[%d]\t%d\t|%s" % (i, linea_dic[i][0], linea_dic[i][1])

    return linea_dic


def checar_indent(linea_dic):
    '''
    dict(num_linea: [indentacion, linea]) -> list(mensajes_error)

    Usa un diccionario con el numero de linea, el nivel de indentaciom,
    y la linea misma por cada linea del codigo, retorna un lista con
    mensajes de error indicando la linea, donde ocurrio el error, si es
    que los hubo.
    '''

    mensajes = []

    # Evita que el código de la primera línea tenga indentación mayor que 0.
    if linea_dic[1][1][0] == "\t":
        mensajes.append("Error de indentación en la línea [1]")

    for i in range(len(linea_dic)):

        i += 1

        # No checa líneas vacías.
        if i > 1 and linea_dic[i][1] != " ":

            ii = i

            # Almacena el último caracter de la línea anterior siempre que la línea anterior no sea vacía.
            while ii > 1:
                if linea_dic[ii-1][1] != " ":
                    ultimo = linea_dic[ii-1][1][-1]
                    break
                ii -= 1

            # Almacena el valor de indentación de la línea anterior.
            inden_anterior = linea_dic[ii-1][0]

            # Almacena el valor de indentación de la línea actual.
            inden_actual = linea_dic[i][0]

            # Controla la indentación en relación a los últimos ":" y almacena los mensajes de error.
            if ultimo == ":" and inden_anterior >= inden_actual:
                mensajes.append("Error de indentación en la línea [%d]" % i)

            # Detecta error si una línea tiene indentación mayor que la anterior y la anterior no termina en ":".
            elif ultimo != ":" and inden_anterior < inden_actual:
                mensajes.append("Error de indentación en la línea [%d]" % i)

    return mensajes


def main():
    '''
    Ejecuta el programa principal.

    Imprime errores de haber habido inconsistencias de indentacion
    en el codigo.
    '''

    codigo_input = obtener_input()
    codigo_indent = calcular_indent(codigo_input)
    mensajes = checar_indent(codigo_indent)

    if mensajes != []:
        for mensaje in mensajes:
            print mensaje
    else:
        print "\nIndentación correcta.\n"

# Se ejecuta main() cuando se corre como...  "$ python2 Sem7Des1_Colaborativo.py"
#  desde la terminal pero no cuando se importa el archivo como un modulo desde otro
# programa o desde la sesion interactiva.

if __name__ == '__main__':
    main()
