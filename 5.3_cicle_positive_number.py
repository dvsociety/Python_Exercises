"""
Ejercicio 5.3. nos piden que escribamos una función que le pida al usuario que ingrese un
número positivo. Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar
de su error mediante un mensaje y volverle a pedir el número.
Resolver este problema usando
1. Un ciclo interactivo.
2. Un ciclo con centinela.
3. Un ciclo “infinito” que se corta.

"""

def interactive_cicle():
    confirm = "si"
    while confirm == "si":
        number = int(input("ingrese un numero positivo "))
        if number < 0:
            print("El numero debe ser mayor a 0")
            continue
        confirm = input("Quiere seguir? <si-no> ").lower()

interactive_cicle()

def read_centinel():
    return input("ingrese un numero positivo (* para terminar) ")

def centinel_cicle():
    centinel = read_centinel()
    while centinel != "*":
        number = int(centinel)
        if number < 0:
            print("El numero debe ser mayor a 0 ")
        centinel = read_centinel()

# centinel_cicle()

def infinite_cicle():
    while True: 
        centinel = input("ingrese un numero positivo (* para terminar) ")
        if centinel == "*":
            break

        number = int(centinel)
        if number < 0:
            print("El numero debe ser mayor a 0 ")

# infinite_cicle()
