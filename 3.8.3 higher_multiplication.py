"""
Ejercicio 3.8.3. Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4).
"""

def higher_multiplication(number_one, number_two, number_three, number_four):
    return max(number_one * number_two, number_one * number_three, number_one * number_four,
            number_two * number_three, number_two * number_four, number_three * number_four)

print(higher_multiplication(-2,-8,-5,30))

# Version con listas 
def higher_multiplication_list(number_one, number_two, number_three, number_four):
    list_numbers = [number_one, number_two, number_three, number_four]
    list_numbers.sort()  
    if list_numbers[0] > 0:
        return list_numbers[-1] * list_numbers[-2] 
    elif list_numbers[-1] < 0:
        return list_numbers[0] * list_numbers[1]
    else: 
        return max(list_numbers[0] * list_numbers[1], list_numbers[-1] * list_numbers[-2])

print(higher_multiplication_list(-2,-8,-5,30))
