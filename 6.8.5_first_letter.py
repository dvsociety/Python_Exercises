"""
Ejercicio 6.8.5. Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
devolver 'USB'.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
debe devolver 'Antes ayer'
"""

### --- Version sin listas --- ###

def first_letters(phrase):
    """Devuelve la primer letra de cada palabra (sin usar listas ni funciones predefinidas)"""
    auxiliar = phrase[0]
    for i in range(len(phrase) - 1):
        if phrase[i] + phrase[i + 1] == "  ":
            i += 1
        elif phrase[i] == " ":
            auxiliar += phrase[i + 1]
    return auxiliar


print(first_letters("hola mundo"))

### --- Version conociendo las listas --- ###

# cad = "hola mundo"
# lista = cad.split(" ")
# for palabra in lista:
#     print(palabra[0], end="")


def first_capitalize_letter(phrase):
    """Devuelve la primer letra de cada palabra en mayucula (sin usar listas ni la funcion predefinida capitalize)"""
    auxiliar = phrase[0].upper()
    for i in range(1, len(phrase)):
        if phrase[i - 1] == " ":
            auxiliar += phrase[i].upper()
        else:
            auxiliar += phrase[i]
    return auxiliar


print(first_capitalize_letter("hola mundo"))

# def capitalize_phrase(phrase):
#     word_list = phrase.split(" ")
#     for word in word_list:
#         print(word.capitalize(), end=" ")
# print(capitalize_phrase(phrase))


def only_a_letters(phrase):
    """Devuelve las palabras que empiezan con A (sin usar listas ni funciones predefinidas"""
    phrase = " " + phrase
    auxiliar = ""
    for i in range(len(phrase)):
        if (phrase[i] == "a" or phrase[i] == "A") and phrase[i - 1] == " ":
            for x in range(i, len(phrase)):
                if phrase[x] == " ":
                    break
                else:
                    auxiliar += phrase[x]
            auxiliar += " "
    return auxiliar


print(only_a_letters("ahola mundo andale"))
