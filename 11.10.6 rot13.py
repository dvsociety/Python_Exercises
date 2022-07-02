"""
Ejercicio 11.10.6. Escribir un programa, llamado rot13.py que reciba un archivo de texto de
origen y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea
cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter
comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un
nuevo caracter.
"""

def rot13(source_file: str, target_file: str):
    """

    Args:
        source_file (str): Archivo de origen
        target_file (str): Archivo de destino

    Returns:
        str: texto que quedó en el archivo luego de la rotación de caracteres
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out_phrase = ""

    with open(source_file,"rt") as file:
        text = file.read()
        for char in text.lower():
            if char in alphabet:
                out_phrase += alphabet[(alphabet.find(char)+13)%26]
            else:
                out_phrase += char

    with open(target_file,"w+") as file:
        file.write(out_phrase)
        file.seek(0)
        return file.read()
        
print(rot13("archivos/head.txt","archivos/rot13.txt"))
