def miEdad():
    anioActual = int( input("Año Actual:") )

    calculaEdad( anioActual )
    calculaEdad( anioActual )
    calculaEdad( anioActual )

def calculaEdad( anio ):
    nombre = input("Dame tu nombre: ")
    anioNacimiento = int( input("Año de nacimiento: ") )

    print("-> ", nombre, " este año cumples: ", anio - anioNacimiento, " año(s)")


miEdad()
