"""
Ejercicio 3.1. Escribir una función repite_hola que reciba como parámetro un número entero
n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n .
"""
def repeat_hello(n: int) -> str:
    """_summary_

    Args:
        n (int): Number of times of repeat

    Returns:
        str: N times of word
    """    
    return 'Hola ' * n

print(repeat_hello(3))