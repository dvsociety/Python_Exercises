"""
Ejercicio 4.6.5. Escribir funciones que resuelvan los siguientes problemas:
"""

# a) Dado un año indicar si es un año biciesto
# un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# excepto que también sea divisible por 400.

def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# print (leap_year(400))

# b) Dado un mes, devolver la cantidad de días correspondientes.
def month_days(month):
    if month >= 3 and month <= 12 or month == 1:
        if month <= 7:
            if month % 2 == 0:
                daysOfTheMonth = 30
            else:
                daysOfTheMonth = 31
        elif month % 2 == 0:
            daysOfTheMonth = 31
        else:
            daysOfTheMonth = 30
    elif month == 2:
        daysOfTheMonth = 28
    else:
        return "No existen más de 12 meses en el calendario gregoriano"
    return daysOfTheMonth

# print (month_days(5))

# funcion extra para evitar repetir codigo
# devuelve la cantidad de días del mes teniendo en cuenta el año bisiesto
def complete_month_days(month,year):
    if month == 2 and leap_year(year) == True:
        daysOfTheMonth = 29
    else:
        daysOfTheMonth = month_days(month)
    return daysOfTheMonth

# Devuelve la cantidad de días que tiene el año
def year_days(year):
    if leap_year(year) == True:
        totalDaysOfTheYear = 366
    else:
        totalDaysOfTheYear = 365
    return totalDaysOfTheYear

# print(year_days(400))

# c) Dada una fecha (día, mes, año), indicar si es válida o no.
def valid_date(day,month,year):
    if day > 0 and month > 0 and year > 0:
        daysOfTheMonth = complete_month_days(month, year)
        if daysOfTheMonth >= day and month <= 12 and year > 0:
            return True
        else:
            return False
    else:
        return False

# print (valid_date(1,1,400))

# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
def remaining_days_month(day,month,year):
    if valid_date(day, month, year) == True:
        daysOfTheMonth = complete_month_days(month, year)
    else:
        return 'fecha invalida'
    return daysOfTheMonth - day

# print (remaining_days_month(29,2,400))

# e) Dada una fecha, indicar los días que faltan hasta fin de año.
def remaining_days_year(day,month,year):
    sumDays = 0
    if valid_date(day,month,year) == True:
        totalDaysOfTheYear = year_days(year)
        if month == 1:
            return totalDaysOfTheYear - day 
        else: 
            for months in range (2, month+1):
                sumDays += complete_month_days(months, year)
            return totalDaysOfTheYear - (day + sumDays)
    else:
        return "fecha invalida"

# print(remaining_days_year(10, 12, 1990))

# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
def days_passed(day,month,year):
    sumDays = 0
    if valid_date(day,month,year) == True:
        if month == 1:
            return day
        else:
            for months in range (2, month+1):
                sumDays += complete_month_days(months, year)
            return day + sumDays
    else:
        return "fecha invalida"

# print (days_passed(31,12,400))

# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
# entre ambas, en años, meses y días.
def time_passed_between_two_dates(day1,day2,month1,month2,year1,year2):
    if days_passed(day1,month1,year1) >= days_passed(day2,month2,year2):
        higherDate = days_passed(day1,month1,year1)
        lessDate = days_passed(day2,month2,year2)
    else:
        higherDate = days_passed(day2,month2,year2)
        lessDate = days_passed(day1,month1,year1)
    if year1 >= year2: 
        higherYear = year1
        lessYear = year2
    else:
        higherYear = year2
        lessYear = year1
    differenceDateInDays = higherDate - lessDate
    differenceOfYears = higherYear - lessYear
    differenceOfMonths = int(differenceDateInDays/30) #hecho en promedio para avanzar a otros ejericios
    differenceOfDays = (differenceDateInDays%30) 
    return (differenceOfDays, differenceOfMonths, differenceOfYears)

print (time_passed_between_two_dates(1,1,1,3,2020,1990))
print (days_passed(1,1,2020))
print (days_passed(1,3,1990))
