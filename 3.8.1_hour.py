"""
Ejercicio 3.8.1. Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos.
"""

def to_seconds(hour, minute, second) -> int:
    """_summary_

    Args:
        hour (_type_): Hours
        minute (_type_): Minutes
        second (_type_): Seconds

    Returns:
        int: time in seconds
    """    
    add_seconds = hour * 3600 + minute * 60 + second
    return add_seconds
print(to_seconds(1, 1, 1))

# Version "one liner"
to_seconds_lambda = lambda hour,minute,second:(hour*3600 + minute*60 + second)
print(to_seconds_lambda(1, 1, 1))


def to_time(seconds_received) -> tuple:
    """_summary_

    Args:
        seconds_received (_type_): Total seconds

    Returns:
        tuple: Hour, minutes and seconds
    """    
    hour = int(seconds_received / 3600)
    minute = int((seconds_received % 3600) / 60)
    second = int((seconds_received % 3600) % 60)
    return (hour, minute, second)

print(to_time(63))
