"""
Ejercicio 7.10.
a) Procesamiento de telegramas. Un oficial de correos decide optimizar el trabajo
de su oficina cortando todas las palabras de más de cinco letras a sólo cinco letras (e indicando
que una palabra fue cortada con el agregado de una arroba). Además elimina todos los espacios
en blanco de más.
Por ejemplo, al texto "Llego mañana alrededor del mediodía" se transcribe
como "Llego mañan@ alred@ del medio@".
Por otro lado cobra un valor para las palabras cortas y otro valor para las palabras largas
(que deben ser cortadas).
b) Los puntos se reemplazan por la palabra especial ”STOP”, y el punto final (que puede
faltar en el texto original) se indica como ”STOPSTOP”.
Al texto:
"Llego mañana alrededor del mediodía. Voy a almorzar "
Se lo transcribe como:
"Llego mañan@ alred@ del medio@ STOP Voy a almor@ STOPSTOP".
"""

def telegram(text: str):
    new_text = ""
    list_text = text.split()
    for palabra in list_text:
        if len(palabra) > 5: 
            new_text += palabra[:5] + "@ "
        else:
            new_text += palabra + " "
    return new_text

# print(telegram("hola mundo gaturro"))

def telegram2(text: str):
    new_text = ""
    for letra in text:
        if letra == ".":
            new_text += " STOP"
        elif letra != ".":
            new_text += letra
    if text[-1] == ".":
        new_text += "STOP"

    list_text = new_text.split()
    aux_list_text = []
    for palabra in list_text:
        if len(palabra) > 5 and palabra != "STOPSTOP":
            aux_list_text.append(palabra[:5] + "@")
        else:
            aux_list_text.append(palabra)
    final_text = " ".join(aux_list_text)
    return final_text

print(telegram2("hola mundo. reloco."))
