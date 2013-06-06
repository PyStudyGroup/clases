


def obtDatos():
    dato1 = input('Tamanho de la barra1: ')
    dato2 = input('Tamanho de la barra2: ')
    dato3 = input('Tamanho de la barra3: ')
    dato4 = input('Tamanho de la barra4: ')
    datosLista=[dato1,dato2,dato3,dato4]    
    return datosLista

def ResPant():
    tamanhoMax = input('Tamanho Maximo: ')
    rango = range(0,tamanhoMax)
    datos = obtDatos()
    limit = 23*"+"
    barra = 4*"-"
    dato1 = datos[0]
    dato2 = datos[1]
    dato3 = datos[2]
    dato4 = datos[3]
    print "El alcance de la barra es: %d" % tamanhoMax
    print limit
    for i in rango:
        if dato1 >= tamanhoMax:
            barra1 = barra
        else:
            barra1= "    "
        if dato2 >= tamanhoMax:
            barra2 = barra
        else:
            barra2 = "    "
        if dato3 >= tamanhoMax:
            barra3 = barra
        else:
            barra3= "    "
        if dato4 >= tamanhoMax:
            barra4 = barra
        else:
            barra4= "    "  
 
        print "+ %s %s %s %s +" % (barra1,barra2,barra3,barra4)
        tamanhoMax -= 1
    print limit  
    raw_input('(exit)')
    return
ResPant()