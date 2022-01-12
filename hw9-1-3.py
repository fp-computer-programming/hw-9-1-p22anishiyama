# Author: ATN 1/12/22

def find_thing(item, term):
    if(type(item) == str):
        return item.find(term)
    else:
        for i, v in enumerate(item):
            if(v != term):
                continue
            elif v == term:
                return(v)
            else:
                return(-1)


print(find_thing(['testing', 'this', 'statement'], 'statement'))
print(find_thing('testing', 'g'))
print(find_thing('testing', 'm'))
