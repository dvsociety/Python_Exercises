"""
Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del final al
principio.
"""
def reverse_string():
    sentence = "hola mundo!"
    for count in range(1, len(sentence) + 1):
        print(sentence[count - 1])
