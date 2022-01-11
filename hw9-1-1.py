# Author: ATN 1/10/22

def even_values(lst):
    numbers = []
    for i, v in enumerate(lst):
        if(v % 2 != 0):
            continue
        else:
            numbers.append(v)
    return numbers


print(even_values([2, 7, 8]) == [2, 8])
