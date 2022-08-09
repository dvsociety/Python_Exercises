"""
Ejercicio 9.5.3. Continuación de la agenda.
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”end”, para salir del programa.
"""
import random

def random_phone():
    """
    Genera telefonos aleatorios para agilizar el calendario
    """
    digits = "1","2","3","4","5","6","7","8","9","0"
    phone = "11"
    for i in range(7):
        phone += random.choice(digits)
    phone = int(phone)
    return phone

def calendar():
    diary = {}
    
    while True:
        centinel = input(str("Nombre a agendar ('end' para terminar) "))
        if centinel == "end":
            break

        name = centinel
        if name not in diary:
            # diary[name] = random_phone()
            diary[name] = int(input(f"Ingrese el telefono de {name} "))
        else:
            print(f"El nombre ya se encuentra en la agenda con el numero: {diary[name]} ")
            print("Si el numero no es correcto, puede modificarlo ") 
            print("¿Desea modificar el numero? ")
            if input(str()) == "si":
                diary[name] = int(input(f"Ingrese el nuevo telefono de {name} "))
    
    return diary

print(calendar())
