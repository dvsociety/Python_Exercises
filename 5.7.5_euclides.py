"""
Ejercicio 5.7.5. Algoritmo de Euclides

Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
números n y m, dado por los siguientes pasos.
1. Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
2. Si r es cero, n es el mcd de los valores iniciales.
3. Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
"""

def euclides(m,n):
    if n == 0: 
        return m
    else: 
        r = m % n
        return (euclides(n,r))
print (euclides(2366,273))
