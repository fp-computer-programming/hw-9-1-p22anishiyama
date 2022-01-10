# Author: ATN 1/10/22

def even_values(lst):
    for i, v in enumerate(lst):
        if(lst[v] % 2 != 0):
            del(lst[v])
            continue