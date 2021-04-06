def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 2:
        return None
    
    if ints[0]> ints[1]:
        minval = ints[1]
        maxval = ints[0]
    else:
        minval = ints[0]
        maxval = ints[1]
    
    for i in range(2, len(ints)):
        if ints[i] < minval:
            minval = ints[i]
        if ints[i] > maxval:
            maxval = ints[i]
    return (minval, maxval)
        




## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")