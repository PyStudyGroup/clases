# python v3.3.0
i=1
fecha=input ("En que año estamos?:")
while i<=3:
    nombre=input ("Dame tu nombre:")
    anno=input ("En que año naciste?:")
    edad=int(fecha)-int(anno)
    print ("Este año ", nombre, "cumples ",edad," años")
    i=i+1
