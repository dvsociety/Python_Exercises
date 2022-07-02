"""
Ejercicio 11.10.4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e im-
prima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.
"""

def file_info(file_name: str):
    """Dado un archivo, informa la cantidad de lineas, palabras y caracteres que este posee

    Args:
        file_name (str): Nombre del archivo

    Returns:
        str: Cantidad de lineas, palabras y caracteres
    """
    count_characters = 0
    count_lines = 0
    count_words = 0 

    with open(file_name,"r") as file:

        for line_number, line in enumerate(file):
            # line = line.rstrip("\n")
            count_characters += len(line)
            count_lines = line_number + 1
            count_words += len(line.split())

    return f"Lineas = {count_lines}, palabras = {count_words}, caracteres = {count_characters}"

print(file_info("archivos/head.txt"))

def file_info_v2(file_name: str):
    """Dado un archivo, informa la cantidad de lineas, palabras y caracteres que este posee (version más rapida)

    Args:
        file_name (str): Nombre del archivo

    Returns:
        str: Cantidad de lineas, palabras y caracteres
    """
    count_characters = 0
    count_lines = 0
    count_words = 0 

    with open(file_name,"r") as file:

        text = file.read()
        file.seek(0)
        count_lines = len(file.readlines())
        file.seek(0)
        count_characters = len(text)
        file.seek(0)
        count_words = len(text.split())

    return f"Lineas = {count_lines}, palabras = {count_words}, caracteres = {count_characters}"

print(file_info_v2("archivos/head.txt"))

