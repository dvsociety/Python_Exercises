"""
Ejercicio 3.8.3. Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4).
"""

def multiplication(number_one,number_two):
    return (number_one * number_two)

def higher_multiplication():
    aux = 0 
    max = 0
    for i in range (0,5):
        number_one = (int(input("numero 1 ")))     
        number_two = (int(input("numero 2 ")))     
        aux = multiplication(number_one,number_two)
        if i == 0: 
            max = aux
        elif max < aux:
            max = aux
    return max

# print(higher_multiplication())
