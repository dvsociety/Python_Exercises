"""
Ejercicio 5.7.7. Números perfectos y números amigos

a) Escribir una función que devuelva la suma de todos los divisores de un número n, sin incluirlo.
b) Usando la función anterior, escribir una función que imprima los primeros m números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).
c) Usando la primera función, escribir una función que imprima las primeras m parejas
de números ( a , b ), tales que la suma de los divisores de a es igual a b y la suma de los
divisores de b es igual a a (es decir las primeras m parejas de números amigos).
"""

def dividers(n):
    """Devuelve la suma de los divisores del numero n"""
    sum_dividers = int(0) 
    for i in range (1, int((n / 2) + 1)):
        if n % i == 0:
            sum_dividers += i
    return sum_dividers

# print(dividers(4))

def perfect_numbers(m):
    """Devuelve los numeros perfectos hasta llegar al numero m"""
    list = []
    for i in range (1,m+1):
        if dividers(i) == i:
            list.append(i)
    return list

# print(perfect_numbers(800))

def friends_numbers(m):
    for i in range (1,m):
        sum_dividers_i = int(dividers(i))
        for j in range (1,m):
            sum_dividers_j = int(dividers(j))
            if sum_dividers_i == j and sum_dividers_j == i and j != i:
                print(f'El numero {i} y el numero {j} son amigos')

friends_numbers(285)
# --------- no logro encontrar forma de que solo se repita una vez los pares de numeros ---------
