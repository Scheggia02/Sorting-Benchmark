from timeit import time
from random import randrange

# Mi riscrivo una funzione che trova il minimo di una lista
# Lista di partenza da ordinare

# Algoritmo di ordinamento
def min_element_index(start_index, list):
    result_index = start_index
    for index in range(start_index, len(list)):
        if list[index] < list[result_index]:
            result_index = index
    return result_index

def selection_sort(list):
    start_time = time.time() 

    for idx in range(len(list)):
        min_index = min_element_index(idx, list)
        list[idx], list[min_index] = list[min_index], list[idx]
    
    stop_time = time.time()
    return start_time - stop_time

