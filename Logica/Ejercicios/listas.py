#LISTAS
'''
se declaran suando corchetes, puede ser vacio
contiene un grupo de elementos
pueden ser de diferentes tipos de datos
se accede a sus elementos por su indice
se pueden modificar, agregar y eliminar elementos
'''

carros = ["Toyota", "Mazda", "Hyundai", "Kia"]
print(carros) #imprime toda la lista

#indexacion
carros[0] = "Renault" #modifica el primer elemento
print(carros)

#concatenacion
carros2 = ["Chevrolet", "Ford"]
carros3 = carros + carros2 #une dos listas
print(carros3)


#repeticion de elementos
carros4 = carros * 2 #repite la lista
print(carros4) #['Renault', 'Mazda', 'Hyundai', 'Kia', 'Renault', 'Mazda', 'Hyundai', 'Kia']

#Pertenencia 
resultado = "Kia" in carros #devuelve True si el elemento esta en la lista
print(resultado)

resultado = "Audi" not in carros #devuelve True si el elemento no esta en la lista
print(resultado)

#Splits como tal son una funcion de string pero devuelve una lista
lista_split = "hola mundo como estan"
resultado = lista_split.split() #por defecto separa por espacios
print(resultado) #['hola', 'mundo', 'como', 'estan']

lista_split = "hola \tmundo \tcomo estan"
resultado = lista_split.split() #separa por tabulaciones
print(resultado) #['hola', 'mundo', 'como', 'estan']

lista_split = "hola,mundo,como,estan"
resultado = lista_split.split(",") #separa por comas o pueden ser puntos
print(resultado) #['hola', 'mundo', 'como', 'estan']

#desempraquetado 
cadena = input("Ingrese su nombre completo: ")
nombres = cadena.split() #separa por espacios
print(nombres)

#join() une los elementos de una lista en un string
nuevo_string = " ".join(nombres) #une con espacios
print(nuevo_string) #Juan Perez Gomez

#len() devuelve la cantidad de elementos de una lista
print(carros) #['Renault', 'Mazda', 'Hyundai', 'Kia']
print(len(carros)) #4

for i in range(3):
    print(carros)

#sum
lista_numeros = [1, 2, 3, 4, 5.5]
total = sum(lista_numeros) #suma todos los elementos de la lista
print(total) #15

#append agrega un elemento al final de la lista
carros.append("Chevrolet") 
print(carros) #['Renault', 'Mazda', 'Hyundai', 'Kia', 'Chevrolet']

#insert agrega un elemento en una posicion especifica
carros.insert(7, "Audi") #agrega Audi en la posicion 1
#si se pone un indice mayor al tamaño de la lista lo agrega al final
print(carros) 

#pop elimina un elemento de la lista y lo devuelve
print(carros) 
eliminado = carros.pop() #elimina el ultimo elemento
print(eliminado) 

print("***************************************")
print(carros) 
carros.pop(1) #elimina el elemento en la posicion 1
print(carros) 

#remove elimina un elemento especifico de la lista, no por indice
print("***************************************")
print(carros) 
carros.remove("Kia") #elimina Kia de la lista  
print(carros) 
#si el elemento no existe da error

#del elimina un elemento por su indice
'''
tambien puede elimianr una lista completa del espacio de memoria   
'''
print("***************************************")
print(carros) 
del carros[0] #elimina el elemento en la posicion 0
print(carros) 

#index devuelve la posicion de un elemento
print("***************************************")
print(carros) 
pos = carros.index("Hyundai") #devuelve la posicion de Hyundai
print(pos) 

#count devuelve la cantidad de veces que un elemento se repite en la lista
print("***************************************")
numeros = [1, 2, 3, 4, 1, 5, 1]
print(numeros)
cantidad = numeros.count(1) #devuelve la cantidad de veces que se repite el 1
print(cantidad) 

#sorted ordena una lista y devuelve una nueva lista
#ordena de menor a mayor
print("***************************************")
lista1 = [1, 13, 9]
lista2 = sorted(lista1) #devuelve True si todos los elementos son iguales
print(lista1)
print(lista2)
lista3 = sorted(lista1, reverse=True) #ordena de mayor a menor
print(lista3)

#cast list retorna una lista a partir de una cadena
print("***************************************")
cadena = "Hola Mundo"
lista = list(cadena) #convierte la cadena en una lista de caracteres
print(lista)

