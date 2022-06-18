"""
Ejercicio 6.8.2. Escribir funciones que dada una cadena y un caracter:
"""

#  Inserte el special_character entre texta character de la textena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'
def coma_character():
    text = "separar"
    special_character = ","
    auxiliar = ""

    for character in text:
        auxiliar += character + special_character
    return auxiliar[:-1]


print(coma_character())

# Reemplace todos los espacios por el special_character. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'
def character_underscore():
    text = "mi archivo de texto.txt"
    special_character = "_"
    auxiliar = ""

    for character in text:
        if character == " ":
            auxiliar += "_"
        else:
            auxiliar += character
    return auxiliar


print(character_underscore())

# Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver '255.255.255.0'
def ip_number():
    text = "123456789123"
    auxiliar = ""
    count = 0

    for i in text:
        count += 1
        if count == 3:
            auxiliar += i + "."
            count = 0
        else:
            auxiliar += i

    if auxiliar[-1] == ".":
        return auxiliar[:-1]
    else:
        return auxiliar


print(ip_number())
