"""
Ejercicio 6.1. Escribir un ciclo que permita mostrar los caracteres de una cadena del final al
principio.
"""
sentence = "hola mundo!"

def reverse_string(string_to_invert: str):
    """_summary_

    Args:
        sentence (str): string to invert
        
    Returns: 
        str: string invertido
    """    
    
    new_string = ''

    for i in string_to_invert: 
        new_string = i + new_string
    
    return new_string

print(reverse_string(sentence))