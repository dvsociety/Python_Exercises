"""
Problema 6.1. Queremos contar cuántas letras “A”
hay en una cadena s.
"""

def count(character, word):
    auxiliar_count = 0
    for letter in word:
        if letter == character.lower():
            auxiliar_count += 1
    return auxiliar_count


print(count("i", "gatiiiiinnn"))
