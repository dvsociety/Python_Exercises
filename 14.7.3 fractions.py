"""
Ejercicio 14.7.3. Fracciones
a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.
b) Crear un método sumar que recibe otra fracción y devuelve una nueva fracción con la
suma de ambas.
c) Crear un método multiplicar que recibe otra fracción y devuelve una nueva fracción
con el producto de ambas.
d) Crear un método simplificar que modifica la fracción actual de forma que los valores
del dividendo y divisor sean los menores posibles.
"""

class Fractions():

    def __init__(self, dividend, divider):
        self.dividend = dividend 
        self.divider = divider

    def __str__(self):
        return f"{self.dividend}/{self.divider}"

    def result(self):
        return round((self.dividend / self.divider),2)

    def addition(self, other_fraction):
        return self.result() + other_fraction.result()

    def multuply(self, other_fraction):
        return self.result() * other_fraction.result()

    def simplify(self):
        for i in range(2,9):
            while self.dividend % i == 0 and self.divider % i == 0:
                self.dividend //= i
                self.divider //= i
        return self.dividend, self.divider

x = Fractions(24,10)
# y = Fractions(1,1)
print(x.simplify())

# print(x)
# print(x.addition(y), x.multuply(y))
