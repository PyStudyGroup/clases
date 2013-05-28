Semana 6 - Desadío 1
====================

Telar informático
-----------------

Desarrollar un programa que permita crear diseños a partir de patrones y
desplazamientos:

- Los patrones pueden ser cualquier cadena de caracteres de una misma
longitud y son ingresados por teclado.
- Los patrones forman capas que se superponen. Las de nivel superior se
hubican encima de las de un nivel inferior.
- Para cada capa o patrón se define un desplazamiento que puede ser
nulo, 1 o -1.

Ejemplo 1:
----------

>Esta marca sirve para ayudar al usuario al momento de ingresar los patrones.
>"123456789012"
>"|          |"

<!-- language: lang-bash -->

    ¿Cuántas capas tendrá el diseño?: 3
    ¿Cuál será el ancho del patrón?: 12

    Introduzca el diseño de la capa 0:
    123456789012
    |          |
    ++++++++++++
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 0

    Introduzca el diseño de la capa 1:
    123456789012
    |          |
    \\\\
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 1

    Introduzca el diseño de la capa 2:
    123456789012
    |          |
            ////
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: -1

    ¿Cuántas hiladas tendrá el diseño?: 24

    \\\\++++////
    +\\\\++////+
    ++\\\\////++
    +++\\////+++
    ++++////++++
    +++////\\+++
    ++////\\\\++
    +////++\\\\+
    ////++++\\\\
    ///++++++\\/
    //++++++++//
    /\\++++++///
    \\\\++++////
    +\\\\++////+
    ++\\\\////++
    +++\\////+++
    ++++////++++
    +++////\\+++
    ++////\\\\++
    +////++\\\\+
    ////++++\\\\
    ///++++++\\/
    //++++++++//
    /\\++++++///

Ejemplo 2:
----------

<!-- language: lang-bash -->

    ¿Cuántas capas tendrá el diseño?: 4
    ¿Cuál será el ancho del patrón?: 15

    Introduzca el diseño de la capa 0:
    123456789012345
    |             |
           |       
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 0

    Introduzca el diseño de la capa 1:
    123456789012345
    |             |
    \\\
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 1

    Introduzca el diseño de la capa 2:
    123456789012345
    |             |
                ///
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: -1

    Introduzca el diseño de la capa 3:
    123456789012345
    |             |
    |             |
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 0

    ¿Cuántas hiladas tendrá el diseño?: 24

    |\\    |    //|
    |\\\   |   ///|
    | \\\  |  /// |
    |  \\\ | ///  |
    |   \\\|///   |
    |    \\///    |
    |     ///     |
    |    ///\\    |
    |   ///|\\\   |
    |  /// | \\\  |
    | ///  |  \\\ |
    |///   |   \\\|
    |//    |    \\|
    |/     |     \|
    |\     |     /|
    |\\    |    //|
    |\\\   |   ///|
    | \\\  |  /// |
    |  \\\ | ///  |
    |   \\\|///   |
    |    \\///    |
    |     ///     |
    |    ///\\    |
    |   ///|\\\   |

Ejemplo 3:
----------

<!-- language: lang-bash -->

    ¿Cuántas capas tendrá el diseño?: 2
    ¿Cuál será el ancho del patrón?: 15
    
    Introduzca el diseño de la capa 0:
    123456789012345
    |             |
    \ \ \ \
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: 1
    
    Introduzca el diseño de la capa 1:
    123456789012345
    |             |
            / / / /
    ¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: -1
    
    ¿Cuántas hiladas tendrá el diseño?: 24
    
    \ \ \ \ / / / /
     \ \ \ / / / / 
      \ \ / / / /
       \ / / / /
        / / / /    
       / / / / \
      / / / / \ \
     / / / / \ \ \ 
    / / / / \ \ \ \
    \/ / /   \ \ \/
    /\/ /     \ \/\
    \/\/       \/\/
    /\/\       /\/\
    \/\ \     / /\/
    /\ \ \   / / /\
    \ \ \ \ / / / /
     \ \ \ / / / / 
      \ \ / / / /
       \ / / / /
        / / / /    
       / / / / \
      / / / / \ \
     / / / / \ \ \ 
    / / / / \ \ \ \
