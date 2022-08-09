
"""
Ejercicio 5.7.3. Manejo de contraseñas
"""

import time

# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
# rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
def session_login():
    realPassword = 123456
    while True:
        userPassword = int(input("Introduzca su contraseña "))
        if userPassword == realPassword:
            break
        else:
            print("Contraseña incorrecta")
    return "Iniciando sesión"


# b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
# tos.
def login_attemp():
    realPassword = 123456
    for i in range(1, 6):
        userPassword = int(input("Introduzca su contraseña "))
        if userPassword == realPassword:
            print("Iniciando sesión")
            break
        else:
            print("Contraseña incorrecta")
    return "Ha superado el maximo de intentos, vuelva a intentarlo más tarde"


# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.
def login_attemp_with_time():
    clockTime = 0
    realPassword = 123456
    for i in range(1, 11):
        userPassword = int(input("Introduzca su contraseña "))
        if userPassword == realPassword:
            print("Iniciando sesión")
            break
        else:
            print("Contraseña incorrecta")
            if i % 5 == 0 and i % 10 != 0:
                print(
                    "Si no recuerda su contraseña vaya a la opción 'recuperar contraseña'"
                )
                clockTime += 1
                time.sleep(clockTime)
        # revisaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        if i % 10 == 0:
            clockTime += 5
            print(
                "Ha superado el maximo de intentos, intente recuperar su contraseña y luego vuelva a intentarlo"
            )
            time.sleep(clockTime)
    return "Precaución, su cuenta podría ser bloqueada en caso de seguir fallando su contraseña"


print(login_attemp_with_time())

# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).
