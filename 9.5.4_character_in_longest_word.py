"""
Ejercicio 9.5.4. Escribir una función que reciba un texto y para cada caracter presente en el 
texto devuelva la cadena más larga en la que se encuentra ese caracter.
"""

def character_in_longest_word(text: str):
    list_text = text.split()
    character_in_word = {}
    max_length = 0

    for word in list_text:
        if max_length < len(word):
            max_length = len(word)

        for character in word:
            if max_length == len(word):
                character_in_word[character] = word
            elif character not in character_in_word: 
                character_in_word[character] = word

    return character_in_word

print(character_in_longest_word("No tengo ni idea de como me salio este ejercicio"))
