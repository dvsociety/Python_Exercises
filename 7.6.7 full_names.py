"""
Ejercicio 7.6.7. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
nombre, luego la inicial con un punto, y luego el apellido.
"""

persons = [("Moreno","Pablo","M"),("Spinelli","Irene","B")]

def complete_names(persons: list):
    list_person = []
    for person in persons:
        person = list(person)
        person[0],person[1],person[2] = person[1],person[2] + ".",person[0]
        string_person = " ".join(person)
        list_person.append(string_person)
    return list_person

print(complete_names(persons))
