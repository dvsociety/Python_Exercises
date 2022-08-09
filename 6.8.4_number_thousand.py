"""
Ejercicio 6.8.4. Escribir una función que reciba una cadena que contiene un largo número en-
tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'.
"""

number = str(input("Escriba el numero que quiera seperar cada mil "))


def number_thousand(number):
    count = 0
    aux = ""
    final_number = ""
    for i in range(1, len(number) + 1):
        count += 1
        aux += number[-i]
        if count == 3:
            aux += "."
            count = 0

    for x in range(1, len(aux) + 1):
        final_number += aux[-x]

    if final_number[0] == ".":
        return final_number[1:]
    else:
        return final_number


print(number_thousand(number))
