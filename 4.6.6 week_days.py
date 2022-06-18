"""
Ejercicio 4.6.6. Suponiendo que el primer día del año fue lunes, escribir una función que reciba
un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.
"""

def days_of_the_week(dayOfTheYear):
    if dayOfTheYear <= 366:
        week = dayOfTheYear % 7
        print (week)
        if week == 1:
            return "lunes" 
        elif week == 2:
            return "martes"
        elif week == 3: 
            return "miercoles"
        elif week == 4:
            return "jueves"
        elif week == 5:
            return "viernes"
        elif week == 6:
            return "sabado"
        elif week == 7:
            return "domingo"
    
print (days_of_the_week(15))
