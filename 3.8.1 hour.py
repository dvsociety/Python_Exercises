"""
Ejercicio 3.8.1. Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
"""

def to_seconds(hour, minute, second):
    add_seconds = hour * 3600 + minute * 60 + second
    return add_seconds


print(to_seconds(1, 1, 1))

def to_time(seconds_received):
    hour = int(seconds_received / 3600)
    minute = int((seconds_received % 3600) / 60)
    second = int((seconds_received % 3600) % 60)
    return (hour, minute, second)


print(to_time(63))
