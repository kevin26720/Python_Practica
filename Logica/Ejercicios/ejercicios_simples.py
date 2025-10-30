'''
Cree un programa que solicite un nnumero de 3 digitos y un segundo de 1 digito
mueastre en pantalla true si cumple con:
- los dos ultimos digitos del primer numero es divisible para el segundo numero
- el cuadrado del segundo numero es menor que los dos ultimos digitos del primer numero
y false en caso contrario
'''

num1 = int(input("Ingrese un numero de 3 digitos: "))
num2 = int(input("Ingrese un numero de 1 digito: "))

ultimoss_dos_digitos_num1 = num1 % 100
cuadrado_num2 = num2 ** 2

if ultimoss_dos_digitos_num1 % num2 == 0 and cuadrado_num2 < ultimoss_dos_digitos_num1:
    print("cumple con las dos condiciones?: true")
else:
    print("cumple con las dos condiciones?: false")



#Como formatear cadenas de texto (f-strings)
nombre = "kevin"
edad = 17.66


print(f"Mi nombre es {nombre} y tengo {int(edad)} años")
print(f"Mi nombre es {nombre} y tengo {edad:.1f} años")


'''
Escriba un programa que permita al usuario ingresar las medidas del cateto a y b de un 
triangulo rectangulo, su progrma debera calcular la hipotenuisa c del triangulo a partir 
de la formula del teorema de pitagoras
'''
cateto_a = float(input("Ingrese la medida del cateto a: "))
cateto_b = float(input("Ingrese la medida del cateto b: "))
hipotenusa_c = ((cateto_a)**2 + (cateto_b)**2)**(1/2)
print(f"La hipotenusa c del triangulo es: {hipotenusa_c:.2f}")