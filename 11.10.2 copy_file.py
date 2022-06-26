"""
Ejercicio 11.10.2. Escribir un programa, llamado cp.py, que copie todo el contenido de un ar-
chivo (sea de texto o binario) a otro, de modo que quede exactamente igual.
Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.
"""

def copy_file(file_to_copy: str, paste_file: str):

    if ".txt" in file_to_copy: 
        with open(file_to_copy,"r") as old_file:
            copy = old_file.read()
        with open(paste_file,"w") as new_file:
            new_file.write(copy)
        return "Archivo .txt copiado exitosamente"

    elif ".jpg" or ".png" in file_to_copy:
        with open(file_to_copy,"rb") as old_binary_file:
            copy = old_binary_file.read()
        with open(paste_file,"wb") as new_binary_file:
            new_binary_file.write(copy)
        return "Archivo .jpg copiado exitosamente"

    else:
        return "Tipo de archivo no soportado"

file_name = str(input("Escriba el nombre del archivo a copiar (sin el formato final) "))
file_type = int(input("Ponga '1' para copiar un archivo de texto\nPonga '2' para copiar un archivo binario "))
if file_type == 1:
    print(copy_file(f"archivos/{file_name}.txt", f"archivos/{file_name}_copy.txt"))
elif file_type == 2:
    print(copy_file(f"archivos/{file_name}.jpg", f"archivos/{file_name}_copy.jpg"))


