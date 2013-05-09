# coding=utf-8

def edad():
    """ Esta Funcion pide el año actual ,el nombre
    y el año de nacimiento de 3 usuarios """
    anio_actual = input("Digite el año actual: ")
    print "--------Primer usuario----------------"
    nombre = raw_input("Digite su nombre: ")
    anio_nacimiento = input("Digite el año de su nacimiento: ")
    calcular_edad = anio_actual - anio_nacimiento
    print "--------Segundo usuario---------------"
    nombre1 = raw_input("Digite su nombre: ")
    anio_nacimiento1 = input ("Digite el año de su nacimiento: ")
    calcular_edad1 = anio_actual - anio_nacimiento1
    print "--------Tercer usuario----------------"
    nombre2 = raw_input("Digite su nombre: ")
    anio_nacimiento2 = input ("Digite el año de su nacimiento: ")
    calcular_edad2 = anio_actual - anio_nacimiento2
    print "--------Edad de Los Usuarios----------"
    print "la edad del usuario " + nombre + " Es " + str(calcular_edad) + " años"
    print "la edad del usuario " + nombre1 + " Es " + str(calcular_edad1) + " años"
    print "la edad del usuario " + nombre2 + " Es " + str(calcular_edad2) + " años"
    
 
edad() 

