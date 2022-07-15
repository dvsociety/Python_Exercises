"""
Ejercicio 14.7.2. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 5 billetes
de 10 pesos, 7 monedas de 25 centavos y 4 monedas de 10 centavos).
Se tiene que poder comparar cajas por la cantidad de dinero que hay en cada una, y además
ordenar una lista de cajas de menor a mayor según la cantidad de dinero disponible.
"""

class CashRegister():

    def __init__(self,one_hundred,fifty,ten,five,one):
        self.one_hundred = one_hundred 
        self.fifty = fifty 
        self.ten = ten 
        self.five = five 
        self.one = one 

    def __str__(self):
        return "Cantidad de billetes de cien: {}, de cincuenta: {}, de diez: {}, de cinco: {}, de uno: {}".format(
            self.one_hundred,
            self.fifty,
            self.ten,
            self.five,
            self.one
        )

    def __lt__(self, other_till):
        return self.balance() < other_till.balance()

    def balance(self):
        return self.one_hundred * 100 + self.fifty * 50 + self.ten * 10 + self.five * 5 + self.one * 1

negocio1 = CashRegister(1,4,20,4,34)
negocio2 = CashRegister(5,4,1,4,2)
negocio3 = CashRegister(3,5,9,4,0)
negocios = [negocio1, negocio2, negocio3]

negocios.sort()
for negocio in negocios:
    print(negocio, "- Balance:", negocio.balance())
