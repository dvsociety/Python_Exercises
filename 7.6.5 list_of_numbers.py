"""
Ejercicio 7.6.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números.
"""

list_of_numbers = [-1,1,2,3,4,5,6,7,8,9,10]

def prime(n: int):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True 

def prime_numbers(numbers: list):
    primes = []
    for number in numbers:
        if prime(number) == True:
            primes.append(number)
    return primes

# print(prime_numbers(list_of_numbers))

def average_list(numbers: list):
    sum = 0
    prom = 0
    for number in numbers:
        sum += number
    prom = sum / len(numbers)
    return sum,prom

# print(average_list(list_of_numbers))

def factorials_list(numbers: list):
    factorial = 1
    list = []
    for number in numbers:
        if number > 1:
            for i in range(1,number):
                factorial *= i  
            list.append(factorial)
            factorial = 1
    return list

print(factorials_list(list_of_numbers))
