#coding:utf-8
def saludar():
    print 'Bienvenidos'
    cantidad = int(raw_input('ingrese la cantidad de amigos: '))
    for x in range(cantidad):
        nombre = raw_input('nombre de amigos: ')
        print 'hola %s es un gusto' %(nombre)

    print 'eso es todo'

saludar()
