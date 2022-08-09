"""
Ejercicio 11.10.1. Escribir un programa, llamado head que reciba un archivo y un número N e
imprima las primeras N líneas del archivo.
"""
import os

def create_head(file_name: str):
    """Crea un archivo con el nombre 'head.txt' y su respectivo texto o lo remplaza en caso de que el archivo ya exista

    Args:
        file_name: Nombre que tendrá el archivo

    Returns:
        str: Confirma la creacion del archivo
    """
    file = open(file_name,"w")

    file.write("Hola mundo\neste es mi primer ejercicio\nen Python")

    file.close()
    return "Archivo 'head' creado con exito"

def head(file_name: str, n:int):
    """Abre un archivo y lee las primeras N lineas elegidas

    Args:
        file_name: Nombre que tendrá el archivo
        n (int): Numero hasta el cual se mostraran las lineas de texto del archivo

    Returns: 
        str: Texto vacio para evitar el none
    """
    file = open(file_name,"r")

#Metodo con listas
    # list_file = file.readlines()  
    # for line in range(n):
    #     list_file[line] = list_file[line].rstrip("\n")
    #     print(list_file[line])

#Metodo con ciclo definido
    # for i, line in enumerate(file):
    #     if i < n:
    #         line = line.rstrip("\n")
    #         print(line)

# Metodo con ciclo indefinido
    i = 0
    while i < n:
        line = file.readline().rstrip("\n")
        print(line)
        i += 1

    file.close()

    return ""

print(create_head("archivos/head.txt"))
print(head("archivos/head.txt",2))
# os.remove("archivos/head.txt")
