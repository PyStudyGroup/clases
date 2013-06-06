# python v3.3.0
nom=[]
an=[]
fecha=input ("En que año estamos?:")
for i in range(1,4):
    nombre=input ("Dame tu nombre:")
    nom.append (nombre)
    anno=input ("En que año naciste?:")
    an.append (anno)
    
   
for i in range(0,3):
    edad=int(fecha)-int(an[i])
    print ("Este año ", nom[i], "cumples ",edad," años")
