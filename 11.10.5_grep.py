"""
Ejercicio 11.10.5. Escribir un programa, llamado grep.py que reciba una expresión y un archivo
e imprima las líneas del archivo que contienen la expresión recibida.
"""

def grep(text_to_search: str, file_name: str): 
    """Dada una expresión, la busca e imprime las lineas donde está se encuentra, devuelve una lista vacia en caso de no encontrar nada

    Args:
        text_to_search (str): Texto a buscar
        file_name (str): Nombre del archivo

    Returns:
        list: Lineas de texto con la expresión
    """
    final_lines = []

    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            if text_to_search in line:
                final_lines.append(line)

    return final_lines

print(grep("mundo","archivos/head.txt"))
