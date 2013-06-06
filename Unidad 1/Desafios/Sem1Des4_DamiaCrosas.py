#Grupo de estudio Python #Semana 1 - Desafio 4

#Descripción:
#Dibujar un Rombo del tamaño entrado

#Autor:
#Damià Crosas

def printRhombus(inNumber):

    #Triangulo superior
    top = inNumber
    
    for n in range(inNumber):
        
        #espacios
        for s in range(top):
            print " ",
            
        #2on cuadrante
        for a in range(-1,n):
            a = a + 2
            print a,
            
        #1er cuadrante
        for b in range(n,0,-1):
            print b,
            
        print ""
        top = top - 1

    #Triangulo inferior   
    bottom = inNumber - 2
    printNumb = inNumber
    
    for n in range(1,inNumber):
        
        #espacios
        for s in range(-1,n):
            print " ",
            
        #3er cuadrante
        for a in range(1,printNumb):
            print a,
            
        #4rt cuadrante   
        for b in range(bottom,0,-1):
            print b,
            
        print ""
        printNumb = printNumb - 1
        bottom = bottom - 1
        
            
printRhombus(input("Ingresa un numero:"))
