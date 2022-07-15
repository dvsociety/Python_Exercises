"""
Ejercicio 14.7.4. Vectores
a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
b) Crear un método escalar que reciba un número y devuelva un nuevo vector, con los
elementos multiplicados por ese número.
c) Crear un método sumar que recibe otro vector, verifica si tienen la misma cantidad de
elementos y devuelve un nuevo vector con la suma de ambos. Si no tienen la misma can-
tidad de elementos debe levantar una excepción.
"""

class Vector:

    def __init__(self,x: int,y: int,z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"[{self.x},{self.y},{self.z}]"

    def scalar(self, multiply_number: int):
        return self.x * multiply_number, self.y * multiply_number, self.z * multiply_number

    def addition(self, other_vector):
        if isinstance(other_vector,(list,tuple)) and len(other_vector) == 3:
            other_vector = Vector(*other_vector)
        else:
            raise AttributeError("La longitud del vector no es la adecuada")
        return self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z

vector1 = Vector(1,2,3)
vector2 = (1,2,3,4)
vector3 = Vector(3,2,1)
print(vector1.addition(vector2))
