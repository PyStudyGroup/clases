# python v3.3.0

fecha=input ("En que año estamos?:")
for i in range(1,4):
    nombre=input ("Dame tu nombre:")
    anno=input ("En que año naciste?:")
    edad=int(fecha)-int(anno)
    print ("Este año ", nombre, "cumples ",edad," años")

