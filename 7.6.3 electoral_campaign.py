"""Ejercicio 7.6.3. Campaña electoral
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima el
mensaje Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
"""

def electoral_campaign(nombres: tuple):
    for nombre in nombres: 
        print(f"{nombre} vote por mí ")
        
# print(electoral_campaign(("pepe","pepa","pupo")))

def custom_campaign(nombres: tuple, p: int, n: int):
    for nombre in range(p, p+n):
        print(f"{nombres[nombre]} vote por mí ")

# print(custom_campaign(("a","b","c","d","e"),2,3))

def progre_campaign(nombres: tuple, p: int, n: int):
    for nombre in range(p, p+n):
        if nombres[nombre][-1] == "a":
            print(f"mujer {nombres[nombre]} vote por mí ")
        else:
            print(f"hombre {nombres[nombre]} vote por mí")

print(progre_campaign(("pablo","martin","javier","luciana","eugenia","hernan","micaela"),2,3))
