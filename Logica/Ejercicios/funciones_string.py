#Strings
resultado = "pelota " * 3 # podemos mltiplicar un string por un entero, esto ahce que se presente n veces un string
print(resultado)

#operador in "pertenencia"
resultado = "a" in "manzana" #devuelve True si el string de la izquierda est en el de la derecha
print(resultado)

resultado = "casa" in "el tiene una casa azul"
print(resultado)

#comillas dentro de un string se usa back slash
resultado = "\"Hola Mundo\""
print(resultado)

#saber cantidad de caracteres de una cadena de caracteres
cadena = len("Hola Mundo")
print(cadena) #retorna un entero

#contar caracteres en especifico dentro de una cadena
cadena = "Hola Mundo mundo mundo"
cantidad = cadena.count("do")
print(cantidad) #retorna un entero

#reemplazar caracteres en una cadena
cadena = "Hola Mundo mundo mundo"
nueva_cadena = cadena.replace("mundo", "Python") #reemplaza todas las apariciones
print(nueva_cadena) #puedo usar un replace despues de otro

#borrar caracteres de izquierda y derecha es decir borrar espacios en blanco en los extremos
nombre = "     Juan Perez  "
print(nombre)
cadena = nombre.strip() #elimina espacios en blanco al inicio y al final, tambien podemos poner parametros
#especificar que caracteres eliminar
print(cadena)

#convertir a mayusculas o minusculas
nombre = "Juan Perez"
print(nombre.upper()) #todo a mayusculas
print(nombre.lower()) #todo a minusculas
print(nombre.title()) #primera letra de cada palabra en mayuscula
#print(nombre.upper("Perez")) no se puede no recibe parametros

#conover con que cadena empieza o termina otra cadena
resultado = "hola mundo"
consultar = resultado.startswith("hola") #devuelve True si la cadena empieza con el parametro
print(consultar)
consultar = resultado.endswith("mundo") #devuelve True si la cadena termina con el parametro
print(consultar)


#buscar la posicion de un caracter o substring dentro de una cadena
resultado = "hola mundo"
posicion = resultado.index("mundo") #devuelve la posicion del primer caracter del substring
print(posicion) #si no lo encuentra da error

posicion = resultado.find("hola") #devuelve la posicion del primer caracter del substring
print(posicion) #si no lo encuentra devuelve -1

posicion1 = resultado.index("o") #devuelve la posicion del primer caracter del substring
posicion2 = resultado.index("o", posicion1 + 1) #devuelve la posicion del ultimo caracter del substring
print(posicion1, posicion2) #si no lo encuentra da error

#pertenenecia con un boleano de retorno
resultado = "1443535"
condicion = resultado.isdigit() #devuelve True si todos los caracteres son digitos
print(condicion)

resultado = "Hola Mundo"
condicion = resultado.isalpha() #devuelve True si todos los caracteres son letras
print(condicion)# False por el espacio, tampoco pueden ser puntuicaiones es decir . , : ; etc
#podemos usar islower() para minusculas, isupper() para mayusculas, isalnum() para letras y numeros
