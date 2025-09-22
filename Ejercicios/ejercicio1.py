#Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
# https://www.python.org/


# Crea una variable (y una constante si el lenguaje lo soporta)
# para hacer comentarios de una linea podemos hacerlo con el simnbolo de numerl #
# asi se ve un comentario de una linea

# para hacer comentarios de multiples lineas podemos usar comillas triples """ o '''
'''
asi se ven los comentarios en python si queremos hacerlo en multimples lineas
de esta forma podemos escribir todo lo que queramos sin tenr que añádir el simbolo de numeral enc ada linea
aunque peudo decir que si inicias un comentario con numeral y das espacio la siguiente linea saldra con mumeral
pero esta es una meor forma de hacerlo.
'''

# Crea una variable (y una constante si el lenguaje lo soporta).
'''
Una variable basicamente es un dato que ocupa un espacio de memoria, y como es una variable tambien se puede consultar el dato que almacena,
tampoco podemos usar palabras resevadas del lenguaje como nombre de una variable.

En python no existen constantes como tal pero existen tecnicas para identificarlas, por ejemplo usar mayusculas en el nombre de la variable
edad = 25  # variable
CEDULA = "12345678"  # constante (convención)
Esto difiere de lenguajes como java en los que si existe una sintxis especifica para definir constantes usando la palabra reservada final
int edad = 25 // variable
static final int EDAD = 30 // constante
'''
#- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...)
nombre = "kevin" # cadena de texto o String
edad =25 # entero o int
altura = 1.75 # decimal o float
'''
En python la convencion para declarar variables es snake_case y no camelCase como en otros lenguajes
'''
estado_civil = True # booleano o bool

#Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
print("¡Hola python!")
print(nombre)
print(edad)
print(altura)
print(estado_civil)