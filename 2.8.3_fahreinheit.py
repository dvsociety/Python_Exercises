"""
Ejercicio 2.8.3. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: F = 9
5C + 32
"""

def fahreinheit(f):
    return (f-32)/(9/5)

# print (fahreinheit(100))

def list_fahreinheit():
    aux = 0 
    if aux < 120:
        for i in range (1, 13):
            aux += 10
            print(fahreinheit(aux))
    return

print(list_fahreinheit())
