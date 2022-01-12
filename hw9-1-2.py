# Author: ATN 1/12/22

def odd_values(odds):
    numbers = []
    for i, number in enumerate(odds):
        if(number % 2 != 0):
            numbers.append(number)
        else:
            continue
    return numbers


print(odd_values([1, 4, 6, 9]) == [1, 9])
