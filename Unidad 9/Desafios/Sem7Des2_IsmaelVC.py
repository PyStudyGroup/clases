#!/usr/bin/env python3


from subprocess import call
import sys


agenda = dict()
plantilla = '''
   Nombre:\t{nombre}
 Apellido:\t{apellido}
     Edad:\t{edad}
 Telefono:\t{telefono}
   Correo:\t{correo}
Localidad:\t{localidad}'''


def crear_contacto():
    nombre = input('\nIngresa el nombre: ')
    agenda[nombre] = dict(nombre=nombre)

    apellido_in = input('Ingresa el apellido: ')
    agenda[nombre]['apellido'] = apellido_in if apellido_in != '' else None

    edad_in = input('Ingresa la edad: ')
    agenda[nombre]['edad'] = edad_in if edad_in != '' else None

    telefono_in = input('Ingresa el teléfono: ')
    agenda[nombre]['telefono'] = telefono_in if telefono_in != '' else None

    correo_in = input('Ingresa el e-mail: ')
    agenda[nombre]['correo'] = correo_in if correo_in != '' else None

    localidad_in = input('Ingresa la dirección: ')
    agenda[nombre]['localidad'] = localidad_in if localidad_in != '' else None

    print(plantilla.format(**agenda[nombre]))

    input('\nPulsa enter para continuar.')



def eliminar_contacto():
    print('\nContactos:')

    for indice, contacto in enumerate(sorted(agenda)):
        print("\t%s) %s" % (indice +1, contacto))

    contacto_del = input('\nEscribe el nombre del contacto que deseas eliminar: ')

    try:
        del agenda[contacto_del]
        print('\nContacto eliminado!')
    except KeyError:
        print('\nEl contacto {contacto_del}, no existe!!!'.format(**vars()))

    input('\nPulsa enter para continuar.')



def buscar_contacto():
    print('\nContactos:')

    for indice, contacto in enumerate(sorted(agenda)):
        print("\t%s) %s" % (indice +1, contacto))

    contacto_busq = input('\nEscribe el nombre del contacto: ')

    try:
        print(plantilla.format(**agenda[contacto_busq]))
    except KeyError:
        print('\nEl contacto {contacto_busq}, no existe!!!'.format(**vars()))

    input('\nPulsa enter para continuar.')



def modificar_contacto():
    print('\nContactos:')

    for indice, contacto in enumerate(sorted(agenda)):
        print("\t%s) %s" % (indice +1, contacto))

    contacto_mod = input('\nEscribe el nombre del contacto: ')

    try:
        for indice, llave in enumerate(sorted(agenda[contacto_mod].keys())):
            print('\t%s) %s' % (indice +1, llave))

        modificacion = input('\nSelecciona el numero de la opcion que deseas modificar: ')

        if modificacion == '1':
            apellido_in = input('\nIngresa el apellido: ')
            agenda[contacto_mod]['apellido'] = apellido_in if apellido_in != '' else None

        elif modificacion == '2':
            correo_in = input('\nIngresa el e-mail: ')
            agenda[contacto_mod]['correo'] = correo_in if correo_in != '' else None

        elif modificacion == '3':
            edad_in = input('\nIngresa la edad: ')
            agenda[contacto_mod]['edad'] = edad_in if edad_in != '' else None

        elif modificacion == '4':
            localidad_in = input('\nIngresa la dirección: ')
            agenda[contacto_mod]['localidad'] = localidad_in if localidad_in != '' else None

        elif modificacion == '5':
            nombre_in = input('\nIngresa el nuevo nombre: ')
            agenda[contacto_mod]['nombre'] = nombre_in if nombre_in != '' else None
            agenda[nombre_in] = agenda[contacto_mod]
            del agenda[contacto_mod]

        elif modificacion == '6':
            telefono_in = input('\nIngresa el teléfono: ')
            agenda[contacto_mod]['telefono'] = telefono_in if telefono_in != '' else None

        else:
            print('\nOpcion invalida!!!')

    except KeyError:
        print('\nEl contacto {contacto_mod}, no existe!!!'.format(**vars()))

    input('\nPulsa enter para continuar.')



def main():
    while True:
        call('clear')
        print('''
Bienvenido:

1) Crear nuevo contacto.
2) Eliminar contacto.
3) Buscar contacto.
4) Modificar contacto.
5) Salir.
''')
        opcion = input('¿Que deseas hacer? Selecciona un numero. ')
        if opcion == '1':
            crear_contacto()
        elif opcion == '2':
            eliminar_contacto()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            modificar_contacto()
        elif opcion == '5':
            sys.exit()
        else:
            print('\nOpcion invalida!!!')

        input('\nPulsa enter para continuar.')
    
    

if __name__ == '__main__':
    main()
