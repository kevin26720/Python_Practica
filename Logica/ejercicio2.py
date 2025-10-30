#Ejercicio 2: Operadores Aritméticos y estructuras de control
'''
Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 '''
#Operadores Aritméticos
num1 = 55.25
num2 = 10

print("Suma:", num1 + num2) # Suma
print("Resta:", num1 - num2) # Resta
print("Multiplicación:", num1 * num2) # Multiplicación
print("División:", num1 / num2) # División
print("Módulo:", num1 % num2) # Módulo
print("Exponente:", num1 ** 2) # Exponente
print("División entera:", num1 // num2) # División entera

#Operadores relacionales
print("Igualdad:", num1 == num2) # igual que
print("Desigualdad:", num1 != num2) # distinto que
print("Mayor que:", num1 > num2) # mayor que
print("Menor que:", num1 < num2) # menor que
print("Mayor o igual que:", num1 >= num2) # mayor o igual que
print("Menor o igual que:", num1 <= num2) # menor o igual que

#Operadores lógicos
edad_luis = 18
edad_juan = 20

condicion_and = (edad_luis >= 18) and (edad_juan >= 18) # conjuncion A Y B se cumplen true
print(condicion_and) # True

condicion_or = (edad_luis < 18) or (edad_juan > 18) # disyuncion A O B se cumple true
print(condicion_or) # True

condicion_not = not(edad_luis < 18) # negacion NO A se cumple true
print(condicion_not) # True

#operadores de incremento
num1 += 5 # Equivalente a num1 = num1 + 5
print("Incremento:", num1)

num2 *= 2 # Equivalente a num2 = num2 * 2
print("Multiplicación asignación:", num2)

num1 -= 2 # Equivalente a num1 = num1 - 10
print("Decremento:", num1)

#Operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print("Pertenencia 3 en lista:", 3 in lista) # True
print("Pertenencia 6 en lista:", 6 not in lista) # True

#Operadores de identidad
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Identidad a es b:", a is b) # True
print("Identidad a es c:", a is c) # False
print("No identidad a es c:", a is not c) # True

#Operadores a nivel de bits
x = 10  # En binario: 1010
y = 4   # En binario: 0100 
print("AND a nivel de bits:", x & y)  # AND bit a bit: 0000 -> 0
print("OR a nivel de bits:", x | y)   # OR bit a bit: 1110 -> 14
print("XOR a nivel de bits:", x ^ y)  # XOR bit a bit: 1110 -> 14
print("NOT a nivel de bits:", ~x)      # NOT bit a bit: 0101 -> -11
print("Desplazamiento a la izquierda:", x << 1) # Desplazamiento a la izquierda: 10100 -> 20
print("Desplazamiento a la derecha:", x >> 1) # Desplazamiento a la derecha: 0101 -> 5 


'''
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
'''

#Estructuras condicionales
'''
Escribir un programa que te permita el ingreso de dos nuimero sy muestre en pantalla true si el primer numero
es divisible para el segundo y false si no lo es
'''
num1 = 45
num2 = 7

if num1 % num2 == 0: # CONDIFCIONAL IF ejecuta si la condicion es verdadera
    print("true")
else:
    print("false")

'''
Comparar si el ultimo digito de dos numeros es igual, imprimir true si son iguales y false si no lo son
'''
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
'''
Aqui utilice un condificonal if y utilice el modulo 10 para conocer el ultimo digito de cada numero
'''
if num1 % 10 == num2 % 10:
    print("true")
else:
    print("false")



'''
Crea un progrma que permita ingresar un numero. se debera mostrat true si el numero no estra entre 10 y 100
sin incluirlos extremos
'''

num_solicitado = int(input("ingrese un numero solicitado: "))
if num_solicitado < 10 or num_solicitado > 100:
    print("true")
else:
    print("false")

'''
Escriba un programa que permita al usuario ingresar el radio y altura de un termo de froma cilindrica y calcule
el volumen del termo, debera mostrar true si el usuario puede llebar el termo con 300 ml = 300 cm3 de agua y 
false si no puede
'''

radio = float(input("Ingrese el radio del termo en cm: "))
altura = float(input("Ingrese la altura del termo en cm: "))
volumen = 3.1416 * (radio ** 2) * altura  # Volumen del cilindro: V = πr²h
print("El volumen del termo es: ", volumen, "cm³")
#print(f"El volumen del termo es: {volumen} cm³") el f antes del string permite evaluar expresiones dentro de {}
#print(f"Volumen: {volumen:.2f} cm³")
                          
if volumen >= 300:
    print("Puede llenar el termo con 300 ml de agua?: true")
else:
    print("Puede llenar el termo con 300 ml de agua?: false")


