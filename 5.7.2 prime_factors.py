"""
Ejercicio 5.7.2. Escribir una función que reciba un número entero k e imprima su descomposi-
ción en factores primos.
"""

def prime_factors(number):
    for i in range (2,number+1):
        while number % i == 0:
            print(i)
            number /= i 

prime_factors(45)
