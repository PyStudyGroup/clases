# -*- coding: utf-8 -*-

#Grupo de estudio Python

#Semana 4 - Desafio 1

#Dada una lista de strings, devuelve la lista con los strings ordenados, excepto los que empiezan con "x", que van al principio.

#Autor:
#Carlos Llamacho


def ordenar(datos):
  
  with_x = []
  without_x = []
  for item in datos:
    if item[0] == "x":
      with_x.append(item)
    else:
      without_x.append(item)
      
  without_x = sorted(without_x)
  return with_x + without_x 

if __name__=="__main__":
  print(ordenar(["mix", "xyz", "apple", "xanadu", "aardvark"]))
