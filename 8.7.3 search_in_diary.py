"""
Ejercicio 8.7.3. Agenda simplificada
Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
Debe devolver una lista con todas las tuplas encontradas.
"""

def simplified_diary(word_to_search: str, diary: list):
    found_words = []

    for diary_tuples in diary:
        if word_to_search in diary_tuples[0]:
            found_words.append(diary_tuples)
    
    return found_words

print(simplified_diary("Mar",[("Pablo Martin Moreno",12345678),("Lina Laika", 87654321),("Mar Mar", 9929392)]))
