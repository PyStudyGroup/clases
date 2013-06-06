# Semana 2 - Ejercicio 2
# Python 2.7.4
# @autor: Alejandro Druetta
# Documentación del código

1. Análisis del problema.

Necesitamos un programa que nos diga cuántos libros hemos vendido y cuál
es el valor de la venta discriminando impuestos.

2. Especiﬁcación.

Los datos de entrada serán los siguientes:

- Cantidad de libros vendidos.
- Tasa de impuestos aplicada.
- Título de cada libro vendido.
- Valor de cada libro.

Los datos de salida serán los siguientes:

- Suma del valor de los libros vendidos.
- Suma del total de impuestos aplicados.
        impuesto = (valor libro / 100) * tasa
- Precio total de la venta.
        Precio = Suma valor libros + Suma total impuestos

3. Diseño.

La estructura del programa es simple: entrada, cálculo, salida.

Pseudocódigo:

- Leer cuántos libros se van a vender y referenciarlo con la variable 
  “libros”.
- Leer cuál es la tasa de impuestos aplicada y referenciarlo con la 
  variable “tasa”.
- Definir una función “calc_imuesto(p, t)” que reciba como argumentos 
  “precio” y “tasa” y calcule el valor del impuesto:
        Calcular: impuesto = (p / 100.0) * t
        Retornar impuesto
- Crear un ciclo con un rango igual a la cantidad de libros vendida.
- Leer el título de cada libro y referenciarlo con la variable “titulo”.
- Leer el valor del libro y referenciarlos con la variable “precio”.
- Definir una variable “tot_precio” que acumule el valor de “precio”: 
        tot_precio += precio
- Definir una variable “tot_impuesto” que acumule el cálculo del 
  impuesto aplicado al valor del libro invocando la función 
  “calc_impuesto” con los argumentos “(precio, tasa)”:
        tot_impuesto += calc_impuesto(precio, tasa)
- Mostrar en pantalla la variable “libros”.
- Mostrar en pantalla la variable “tot_precio”.
- Mostrar en pantalla la variable “tot_impuesto”.
- Mostrar en pantalla “tot_precio + tot_impuesto”

4. Implementación.

"https://www.dropbox.com/s/xg1qw4nqqcpw9ug/Sem2Eje1%2BAlejandroDruetta.py"

5. Prueba.

Introducir los siguientes valores:

libros = 1
tasa = 10
título = “cualquiera”
precio = 100

Y verificar que el resultado en pantalla sea igual a:

libros 1
tot_precio 100
tot_impuesto 10
tot_precio + tot_impuesto 110
