#Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
'''
funcion para comparar el ultimo digito entre dos numeros
'''
def comparar_ultimos_digitos(lado1, lado2): # nombramos a la funcion y definimos sus parametros
    if lado1 % 10 == lado2 % 10:
        return True
    else:
        return False

#hacemos un llamado a la funcion
resultado = comparar_ultimos_digitos(35, 364)
print("Resultado de la función:", resultado)


