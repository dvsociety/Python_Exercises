"""
Ejercicio 14.7.1. Modificar el método __lt__ de Hotel para poder ordenar de menor a mayor las
listas de hoteles según el criterio: primero por ubicación, en orden alfabético y dentro de cada
ubicación por la relación calidad-precio.
"""

def valid_positive_number(number: float):
    """
    Si el valor es un numero positivo lo devuelve.
    En caso contrario lanza un error TypeError si no es un numero o
    Exception si no es un numero positivo.
    """
    if not isinstance(number, (int, float)):
        raise TypeError(f"{number} no es un numero")
    if number >= 0: 
        return number 
    else: 
        raise Exception(f"{number} debe ser un numero positivo")

def valid_non_empty_string(text: str):
    """
    Si el valor es un cadena lo devuelve. 
    En caso contrario lanza un TypeError si no es un cadena o
    Exception si es una cadena vacia
    """
    if not isinstance(text, str):
        raise TypeError(f"{text} no es un string")
    if text == None:
        raise Exception(f"{text} no debe ser una cadena vacia")
    else:
        return(text)

class Hotel:

    def __init__(self, name: str, location: str, score: int, price: float):
        self.name = valid_non_empty_string(name)
        self.location = valid_non_empty_string(location)
        self.score = valid_positive_number(score)
        self.price = valid_positive_number(price)

    def __str__(self):
        return (f"{self.name} de {self.location} - Puntaje: {self.score} - Precio: ${self.price}")

    def __lt__(self, other):
        if self.location != other.location:
            return self.location < other.location
        else:
            return self.rate() < other.rate()

    def rate(self):
        return ((self.score ** 2) * 10) / self.price


polo = Hotel("Polo","Buenos Aires",5,40)
polaca = Hotel("Polaca","Buenos Aires",5,46)
wood = Hotel("Wood","Entre Rios",4,39)
holy = Hotel("Holy","Santa Fe",3,30)
hotels = [polo, wood, holy, polaca]

hotels.sort()
for hotel in sorted(hotels):
    print(hotel,"- Ratio:",hotel.rate())
