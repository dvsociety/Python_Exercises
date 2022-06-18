"""
Ejercicio 6.8.6. Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
'logaritmos' debe devolver 'lgrtms'.
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
devolver 'i ooae'.
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
devolver 'vistaerou'.
d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
líndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""

def only_consonants(phrase):
    final_phrase = ""
    for letter in phrase:
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
            or letter == "A"
            or letter == "E"
            or letter == "I"
            or letter == "O"
            or letter == "U"
        ):
            pass
        else:
            final_phrase += letter
    return final_phrase


print(only_consonants("Estas son solo las consonantes"))


def only_vowels(phrase):
    final_phrase = ""
    for letter in phrase:
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
            or letter == "A"
            or letter == "E"
            or letter == "I"
            or letter == "O"
            or letter == "U"
        ):
            final_phrase += letter
        else:
            pass
    return final_phrase


print(only_vowels("Estas son solo las vocales"))


def next_vowel(phrase):
    final_phrase = ""
    for letter in phrase:
        if letter == "a" or letter == "A":
            final_phrase += "e"
        elif letter == "e" or letter == "E":
            final_phrase += "i"
        elif letter == "i" or letter == "I":
            final_phrase += "o"
        elif letter == "o" or letter == "O":
            final_phrase += "u"
        elif letter == "u" or letter == "U":
            final_phrase += "a"
        else:
            final_phrase += letter
    return final_phrase


print(next_vowel("hola mundo como estas"))


def polindromo(phrase):
    count = 0
    for letter in range(len(phrase)):
        if phrase[letter] == phrase[-1 - letter]:
            count += 1
            if count == len(phrase):
                return f"{phrase} es un polindromo"
    return f"{phrase} no es un polindromo"


print(polindromo("hola aloh"))
