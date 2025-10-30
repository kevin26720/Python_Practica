#Indices
palabra = "patineta"

letra = palabra[0]
print(letra) # p
letra = palabra[3]
print(letra) # i

#slicing "se incluide el indice inicial y no el final"
subcadena = palabra[0:4] # desde el indice 0 hasta el 3
print(subcadena) # pati

subcadena = palabra[2::4] # desde el indice 0 hasta el final, con paso 4
print(subcadena) # pa

'''
crea un programa que genere un correo empresarial a partir del ingreso de los diguientes datos:
- primer nombre
- segundo nombre
- primer apellido
- año de nacimiento
formato: primera letra del primer nombre - primera letra del segundo nombre - 
primer apellido - dos ultimos digitos del año de nacimiento @empresa.com
'''

url_empresarial = "www.yahoo.com"
primer_nombre = input("Ingrese su primer nombre: ")
segundo_nombre = input("Ingrese su segundo nombre: ")
primer_apellido = input("Ingrese su primer apellido: ")
anio_nacimiento = input("Ingrese su año de nacimiento: ")

letra1_pn = primer_nombre[0].lower()
letra1_sn = segundo_nombre[0].lower()
primer_apellido_min = primer_apellido.lower()
ultimos2_digitos_anio = anio_nacimiento[-2:]

print(f"Su correo empresarial es: {letra1_pn}{letra1_sn}{primer_apellido_min}{ultimos2_digitos_anio}@{url_empresarial[4:]}")





'''
Usted cuenta con una cadena de caracteres que simula un tweet donde
se mencionan ayudantes de una materia en específico. Ejemplo:
tweet="El día de ayer hubo ayudantías con #Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los"
Asumir que los # solo contienen nombres de ayudantes.
- Mostrar el nombre del primer ayudante
- Mostrar el nombre del segundo ayudante  
- Mostrar el nombre del último ayudante
'''

tweet = "El día de ayer hubo ayudantías con #Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los"

# Encontrar la posición del primer #
pos1 = tweet.index("#")
# Obtener el substring desde la primera # hasta el final
subTweet = tweet[pos1+1: ]
print(subTweet)  # "Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los"

# Encontrar la posición del primer espacio después del primer #
posEsp1 = subTweet.index(" ")
# Extraer el primer nombre de ayudante
ayu1 = subTweet[:posEsp1]
print(ayu1)  # "Joel"

# Encontrar la posición del segundo # en el tweet original (desde después del primer nombre)
pos2_tweet = tweet.index("#", pos1 + 1)
# Obtener substring desde el segundo # hasta el final
subTweet2 = tweet[pos2_tweet+1:]
print(subTweet2)  # "Kevin de CUV ya se divirtieron los pollos, ahora le toca a los"

# Encontrar la posición del segundo espacio después del segundo #
posEsp2 = subTweet2.index(" ")
# Extraer el segundo nombre de ayudante
ayu2 = subTweet2[:posEsp2]
print(ayu2)  # "Kevin"

print(f"Primer ayudante: {ayu1}")
print(f"Segundo ayudante: {ayu2}")

# Para este ejemplo solo hay 2 ayudantes, por lo que el último es el segundo
print(f"Último ayudante: {ayu2}")