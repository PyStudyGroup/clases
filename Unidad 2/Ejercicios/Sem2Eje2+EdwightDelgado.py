#coding:utf-8
#autor EdwightDelgado todo los derechos recervados ....jejeje es broma
"""
Escribir un programa que calcule el costo total de una compra
de libros. Primero pregunta la cantidad de libros y la taza
de impuestos. Luego pregunta el título y el precio de cada
libro. Finalmente, imprime el número de libros, la suma del
valor de los libros, el valor de los impuestos y el total a pagar.
"""
def main():
    pr_total_sin = 0
    pr_total_con = 0
    total_im = 0
    print 'Bienvenido'
    cantidad = int(raw_input('ingrese la cantidad total de libros: '))
    taza = int(raw_input('ingrese la taza de impuestos en %: '))
    for x in range(cantidad):
        titulo = raw_input('ingrese el titulo: ')
        precio_neto = int(raw_input('ingrese el precio: '))
        impuesto = precio_neto * (taza / 100.0)
        precio = precio_neto + impuesto
        print ''
        print 'titulo: ', titulo
        print 'precio sin impuesto: ', precio_neto
        print 'impuesto: ', impuesto
        print 'precio con impuesto: ', precio
        pr_total_sin = pr_total_sin + precio_neto
        pr_total_con = pr_total_con + precio
        total_im = total_im + impuesto
        print ''

    print ''
    print 'usted compro %d libros' %cantidad
    print 'el precio total sin impuesto es %d '%pr_total_sin
    print 'con un total %d impuesto' %total_im
    print 'usted tiene que pagar %d en total ' %pr_total_con

main()

