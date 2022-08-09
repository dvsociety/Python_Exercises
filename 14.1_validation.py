"""
Ejercicio 14.1. Escribir las funciones validar_numero_positivo y validar_cadena_no_vacia,
que deben lanzar TypeError si la validación del valor falla, y en caso contrario simplemente
devolver el valor.
"""

def valid_positive_number(number: float):
    """
    Si el valor es un numero positivo lo devuelve.
    En caso contrario lanza un error TypeError si no es un numero o
    Exception si no es un numero positivo.
    

    Args:
        number (float): Valor a verificar

    Returns:
        float: Devuelve el numero dado
    """
    if not isinstance(number, (int, float)):
        raise TypeError(f"{number} no es un numero")
    if number >= 0: 
        return number 
    else: 
        raise Exception(f"{number} debe ser un numero positivo")

def valid_non_empty_string(text: str):
    """
    Si el valor es un cadena lo devuelve. 
    En caso contrario lanza un TypeError si no es un cadena o
    Exception si es una cadena vacia


    Args:
        text (str): Valor a verificar

    Returns:
        str: Devuelve la cadena dada
    """
    if not isinstance(text, str):
        raise TypeError(f"{text} no es un string")
    if text == None:
        raise Exception(f"{text} no debe ser una cadena vacia")
    else:
        return(text)

print(valid_positive_number(2))
print(valid_non_empty_string("asdsa"))
