"""
El programa genera un número que el jugador no pueda predecir.
Le pide al usuario que introduzca un número de cuatro cifras distintas, y cuando éste lo ingresa, 
procesa la propuesta y evalua el número de aciertos y coincidencias que tiene de acuerdo al código elegido. 
Si es el código original, se termina el programa con un mensaje de felicitación. En caso contrario, 
se informa al jugador la cantidad de aciertos y la de coincidencias, y se le pide una nueva propuesta.
Este proceso se repite hasta que el jugador adivine el código.
"""

import random

CANT_DIGITOS = 4

def elegir_codigo():
    f"""Devuelve un codigo de {CANT_DIGITOS} elegidos al azar"""

    digitos = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    codigo = ""
    for i in range(CANT_DIGITOS):
        candidato = random.choice(digitos)
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo += candidato
    return codigo

def analizar_propuesta(propuesta, codigo):
    """Determina la cantidad de aciertos y coincidencias"""

    aciertos = 0
    coincidencias = 0
    for i in range(CANT_DIGITOS):
        if propuesta[i] == codigo[i]:
            aciertos += 1
        elif propuesta[i] in codigo:
            coincidencias += 1
    return aciertos, coincidencias


def mastermind():
    """funcion principal del juego Mastermind!"""

    print(
        "Bienvenido a Mastermind!\nTienes que adivinar un numero de cuatro cifras distintas"
    )
    codigo = elegir_codigo()
    intentos = 1
    propuesta = input("Que codigo propones ")
    ME_RINDO = "me rindo"

    while propuesta != codigo and propuesta != ME_RINDO:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print(
            f"Tu propuesta {propuesta} tiene {aciertos} aciertos y {coincidencias} coincidencias."
        )
        propuesta = input("Que codigo propones ")

    if propuesta == ME_RINDO:
        return f"Mala suerte, el codigo era {codigo}"
    else:
        return f"Felicitaciones! Adivinaste el codigo en {intentos} intentos"

print(mastermind())

### ________________________________________________________________________###
### VERSION SIMPLIFICADA ###

# import random

# # elegimos el codigo de 4 digitos
# codigo="".join(list(map(lambda x: str(x), random.sample(range(0,9), 4))))

# print ("##### Bienvenido/a al Mastermind! ######\n")
# print ("Tienes que adivinar un numero de 4 cifras distintas")
# propuesta = input("¿Que codigo propones?: ")

# # bucle hasta que el numero introducido coincida con el codigo aleatorio
# intentos = 0
# while propuesta != codigo:
#     intentos += 1
#     aciertos = 0
#     coincidencias = 0

#     # recorremos la propuesta y verificamos en el codigo
#     for i in range(4):
#         if propuesta[i] == codigo[i]:
#             aciertos = aciertos + 1
#         elif propuesta[i] in codigo:
#             coincidencias = coincidencias + 1
#     print ("Tu propuesta (", propuesta, ") tiene", aciertos, "aciertos y", coincidencias, "coincidencias.")
#     # pedimos siguiente propuesta*
#     propuesta = input("Propón otro codigo: ")

# print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
