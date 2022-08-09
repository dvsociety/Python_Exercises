"""
Ejercicio 5.7.8. Escribir un programa que le pida al usuario que ingrese una sucesión de núme-
ros naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
de los valores y el promedio.
"""

def average_natural_numbers():
    total_numbers = 0
    sum_numbers = 0
    average = 0

    while True:
        number = int(input('ingrese un numero (-1 para terminar) '))
        if number < -1:
            print('Ingrese un numero mayor a 0 o -1 para terminar')
            continue
        if number == -1:
            return (f'Total de los numero ingresados: {total_numbers}\nSuma de los numeros ingresados: {sum_numbers} \nPromedio de los numeros ingresados {average}')

        total_numbers += 1
        sum_numbers += number
        average = sum_numbers / total_numbers 


print(average_natural_numbers())
