Desafíos Semana 5
=================

Desafío 1
---------

> Crear una calculadora o conversor binario/digital.
> El menú de entrada sería el siguiente (El programa debe aceptar la opción tanto si el usuario utiliza mayúscula o minúscula):

<!-- language: lang-bash -->

    Calculadora Binario/Decimal

    -----------------------------
    'b' para convertir a Binario.
    'd' para convertir a Decimal.
    's' para salir.
    -----------------------------

    Opción:

> Los resultados se presentarían de la siguiente forma:

<!-- language: lang-bash -->

    Calculadora Binario/Decimal

    -----------------------------
    'b' para convertir a Binario.
    'd' para convertir a Decimal.
    's' para salir.
    -----------------------------

    Opción: b

    -----------------------------
    Digite un decimal: 120
    Resultado:  1111000
    -----------------------------

    'Enter' para continuar.

<!-- language: lang-bash -->
    
    Calculadora Binario/Decimal

    -----------------------------
    'b' para convertir a Binario.
    'd' para convertir a Decimal.
    's' para salir.
    -----------------------------

    Opción: d

    -----------------------------
    Digite un binario: 1111000
    Resultado: 120
    -----------------------------

    'Enter' para continuar.
    
> El programa debe cumplir las siguientes condiciones:

- Detectar una opción diferente a las del menú y dar un mensaje de error.

<!-- language: lang-bash -->

    Opción: g

    -----------------------------
    Opción inválida.
    -----------------------------

    'Enter' para continuar.

- Detectar cuando el número ingresado no es un binario o no es un decimal y dar un mensaje de error.

<!-- language: lang-bash -->

    Opción: b

    -----------------------------
    Digite un decimal: 24gsdf
    24gsdf no es un decimal.
    -----------------------------

    'Enter' para continuar.

- El programa no se detiene hasta que el usuario seleccione la opción 's'.

<!-- language: lang-bash -->

    Opción: s

    -----------------------------
    Fin.

- Opcional: Limpiar la pantalla después de cada "continuar".
