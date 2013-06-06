#Grupo de estudio Python #Semana 1 - Desafio 1

#Descripción:
#Calcular la edad de tres personas basándose en el año actual entrado por teclado.

#Autor:
#Damià Crosas

#Funciones
def checkYear(in_Year):
     if in_Year.isdigit() and len(in_Year) == 4:
          return True
     else:
          return False
     
def getActYear():
     year = 0
     okYear = False     
     while okYear == False:
          year = raw_input("Ingrese el año actual: ")
          okYear = checkYear(str(year))
          if okYear == False:
            print("Atención: Ingrese el año en formato 'aaaa'.")
          print("")
     return int(year)
                  
def printPersonInfo(in_arrNames,in_arrYears,in_arrAges,in_nPersons):
        print( "" )
        for counter in range(in_nPersons):                
                print(in_arrNames[counter] + " nació al año " + in_arrYears[counter] + " y ahora tiene " + in_arrAges[counter] + " años.")
               
def getPersonInfo(in_actYear,out_arrNames,out_arrYears,out_arrAges,in_nPersons):
         for counter in range(in_nPersons):
                name = raw_input("Ingrese el nombre: ")                
                okYear = False     
                while okYear == False:
                     year = raw_input("Ingrese el año de nacimiento: ")
                     okYear = checkYear(str(year))                     
                     if okYear == False:
                          print("Atención: Ingrese un año en formato 'aaaa'.")
                     elif int(year) > in_actYear:
                        okYear = False
                        print("Atención: Ingrese un año inferior al actual") 
                out_arrNames.append(name)
                out_arrYears.append(str(year))
                out_arrAges.append(str(in_actYear - int(year)))
                print("")
                      
def calcAges(in_actYear,in_nPersons):
                      
        #Definiciones de las matrizes
        arrNames  = []
        arrYears  = []
        arrAges   = []

        #Se obtiene la información de la persona
        getPersonInfo(in_actYear,arrNames,arrYears,arrAges,in_nPersons)
       
        #Impresión de los cálculos
        printPersonInfo(arrNames,arrYears,arrAges,in_nPersons) 

#Main      
#Cálculo de la edad de 3 personas basándose en el año entrado
calcAges(getActYear(),3)

