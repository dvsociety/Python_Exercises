"""
Ejercicio 11.10.7. Persistencia de un diccionario
a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
y el segundo como valor.
b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
y guarde el contenido del diccionario en el archivo, con el formato clave, valor.
"""

def load_data(file_name: str):
    """Pasa los datos del archivo a un diccionario

    Args:
        file_name (str): Nombre del archivo

    Returns:
        dict: Información almacenada del archivo
    """
    data = {}

    with open(file_name,"rt") as file:
        for line in file:
            (key,value) = line.split()
            data[key] = value
    # print(data) 
    return data

data = load_data("archivos/dictionary.txt")


def save_data(data: dict, file_name: str):
    """Pasa los datos de un diccionario a un archivo

    Args:
        data (dict): Contenido del diccionario
        file_name (str): Nombre del archivo

    Returns:
        str: Campo vacio para evitar el None
    """
    with open(file_name, "wt") as file:
        for key,value in data.items():
            line = key , value
            file.write(str(line)) 
            file.write("\n")
    return ""

print(save_data(data,"archivos/new.txt"))
