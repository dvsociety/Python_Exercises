"""
Ejercicio 14.7.5. Botella y Sacacorchos
a) Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la
bodega).
b) Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho
que la tapa, o None si está destapada.
c) Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le
saque el corcho y se guarde una referencia al corcho sacado. Debe lanzar una excepción
en el caso en que la botella ya esté destapada, o si el sacacorchos ya contiene un corcho.
d) Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción
en el caso en el que no haya un corcho.
"""

class Cork:
    cellar = "La Gran Bodega"

class Bottle:
    cork = "Corcho madera"

class Corkscrew:
    corkscrew = False

    def uncover(self,bottle):
        if bottle.cork == "Destapado" or self.corkscrew == True:
            raise Exception("Ya está destapado o el sacacorcho tiene un corcho")
        else:
            bottle.cork = "Destapado"
            self.corkscrew = True

    def clean(self):
        if self.corkscrew == True:
            self.corkscrew = False
        else:
            raise Exception("No hay un corcho puesto")

bottle1 = Bottle()
corkscrew = Corkscrew()

corkscrew.uncover(bottle1)
print(bottle1.cork, corkscrew.corkscrew)
corkscrew.clean()
print(corkscrew.corkscrew)
