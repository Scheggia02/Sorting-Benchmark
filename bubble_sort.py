def BubbleSort(_list):
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
    return start_time - stop_time
