from functools import reduce
import operator

def multiple_of_item(items):
    return reduce(operator.mul, items)

print(multiple_of_item([1, 2, 3, 4, 5])) 