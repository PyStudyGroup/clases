#Grupo de estudio Python #Semana 1 - Desafio 3

#Descripción:
#Dibujar un gráfico de barras según valores entrados

#Autor:
#Damià Crosas

#Funciones
def getLine(inSize,inIndex):
      if inSize >= inIndex:
           return "____ "
      else:
           return "     "     
     
def printGraph():
     #Get sizes     
     sizeMax = input("Entre tamaño Máximo:")
     sizeB1 =  input("Entre tamaño Barra 1:")
     sizeB2 =  input("Entre tamaño Barra 2:")
     sizeB3 =  input("Entre tamaño Barra 3:")
     sizeB4 =  input("Entre tamaño Barra 4:")
     
     #Gráfico
     print "+++++++++++++++++++++++" 
     Output = "+ "
     for n in range(sizeMax,0,-1):
           Output = "+ "
           Output = Output + getLine(sizeB1,n)
           Output = Output + getLine(sizeB2,n)
           Output = Output + getLine(sizeB3,n)
           Output = Output + getLine(sizeB4,n)
           print Output + "+" 

     print "+  B1   B2   B3   B4  +"
     print "+++++++++++++++++++++++"
      
#Main      
#Impresión del gráfico
printGraph()


    
        


