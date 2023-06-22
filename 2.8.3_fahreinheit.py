"""
Ejercicio 2.8.3. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = 9
5C + 32
"""

def fahreinheit(f: int) -> int:
    """_summary_

    Args:
        f (int): number to convert

    Returns:
        int: number converted to Celcius
    """    
    return (f-32)/(9/5)

print (fahreinheit(100))
