"""
Ejercicio 15.5.2. Juego de Rol
a) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad,
y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lan-
ce una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una
dirección y se mueva en esa dirección la cantidad indicada por velocidad.
b) Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y
el método atacar, que reciba otro personaje, al que le debe hacer el daño indicado por el
atributo ataque.
c) Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha
y el método cosechar, que devuelva la cantidad cosechada.
"""

class Character:

    def __init__(self):
        self.life = 100
        self.posicion = [0,"north"]
        self.speed = 20

    def receive_atack(self, atack):
        self.life -= atack
        if self.life <= 0:
            raise Exception("Personaje asesinado")

    def move(self, direction):
        self.posicion = [self.speed, direction]
        return self.posicion

class Soldier(Character):

    def __init__(self):
        super().__init__()
        self.strike = 20

    def atack(self, character):
        character.receive_atack(self.strike)

class Farmer(Character):

    def __init__(self):
        super().__init__()
        self.farm = 20

    def harvest(self):
        return self.farm
