"""
Ejercicio 15.5.1. Papel, Birome, Marcador
a) Escribir una clase Papel que contenga un texto, un método escribir, que reciba una
cadena para agregar al texto, y el método __str__ que imprima el contenido del texto.
b) Escribir una clase Birome que contenga una cantidad de tinta, y un método escribir,
que reciba un texto y un papel sobre el cual escribir. Cada letra escrita debe reducir la
cantidad de tinta contenida. Cuando la tinta se acabe, debe lanzar una excepción.
c) Escribir una clase Marcador que herede de Birome, y agregue el método recargar, que
reciba la cantidad de tinta a agregar.
"""

class Paper:
    
    text = "hola mundo estoy programando en python"

    def __str__(self):
        return self.text

    def write(self, words: str):
        self.text += " " + words
        return self.text

class Pen():

    ink = 10

    def write(self, text, paper):
        for i in range(1,len(text)):
            self.ink -= 1 
            if self.ink == 0:
                raise Exception("No hay más tinta")
        return paper.write(text)

class BookMark(Pen):
    
    def charge(self):
        self.ink = 10

paper1 = Paper()
pen1 = Pen()
bookmark1 = BookMark()
print(pen1.write("hola",paper1))
print(bookmark1.write("hola2",paper1))
print(bookmark1.ink)
bookmark1.charge()
print(bookmark1.ink)
print(pen1.ink)
