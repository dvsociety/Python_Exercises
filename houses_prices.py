#Comparación de velocidad de ejecucion entre un for con miles de reiteraciones y una multiplicación de matrices

import numpy as np 
from time import time

houses_sizes = np.random.randint(400, 2000, size=(100000000))

def houses_prices(sizes):
    start_time = time()
    
    houses_values = []
    for i in range(len(houses_sizes)):
        houses_values.append(10190+223*houses_sizes)
        
        end_time = time() - start_time
        print(end_time)
        
        return houses_values

# print(houses_prices(houses_sizes))

def matriz_houses_prices(sizes):
    start_time = time()

    vector_all_one = np.random.randint(1,2, size=(len(houses_sizes)))
    matriz_house_size = np.column_stack((vector_all_one,houses_sizes))
    house_calcules = np.array([10190, 223])
    
    end_time = time() - start_time
    print(end_time)
    
    return np.dot(matriz_house_size, house_calcules)

print(matriz_houses_prices(houses_sizes))