"""
Ejercicio 3.8.2. Usando las funciones del ejercicio anterior, escribir un programa que pida al
usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y mues-
tre por pantalla la duración total en horas, minutos y segundos.
"""
def to_seconds(hour,minute,seconds):
    return(3600 * hour + 60 * minute + seconds)

def to_normal_time(seconds):
    hour = seconds / 3600 
    minute = (seconds % 3600) / 60
    seconds = (seconds % 3600) % 60 
    return(hour,minute,seconds)

def add_seconds():
    add = 0
    N = 2
    for i in range (0,N):
        print(f"tiempo numero: {i+1}")
        hour = int(input("hora "))
        minute = int(input("minutos "))
        seconds = int(input("segundos "))
        add += to_seconds(hour,minute,seconds)
    return add

def main():
    return(to_normal_time(add_seconds()))

print(main())
