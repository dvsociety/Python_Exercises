"""
Ejercicio 3.1. Escribir una función repite_hola que reciba como parámetro un número entero
n y escriba por pantalla el mensaje "Hola" n veces. Invocarla con distintos valores de n .
"""
def repeat_hello(n):
    aux = ""
    for i in range(n):
        aux += "\nhola"
    return aux

print(repeat_hello(3))
