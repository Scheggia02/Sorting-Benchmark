from timeit import time
from random import randrange

# Mi riscrivo una funzione che trova il minimo di una lista
# Lista di partenza da ordinare
mylist = [randrange(1000) for _ in range(10000)]

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
    print(f"{(stop_time-start_time):.7f}")


def OwnBubbleSort(_list):
    start_time = time.time() 

    limit = len(_list) - 1
    while limit > 0:
        for i in range(limit):
            if _list[i] > _list[i + 1]:
                # SWAP ---->
                copy = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = copy
                # ----->
        limit -= 1 #Decrement the range of the Cycle

    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")

OwnBubbleSort(mylist)

# Stampo la lista appena calcolata
print(mylist)

# alla fine voglio che siano soddisfatte le seguenti condizioni
# assert sorted_list[0] == 7
# assert sorted_list[1] == 15
# assert sorted_list[2] == 99
# assert sorted_list[3] == 200
