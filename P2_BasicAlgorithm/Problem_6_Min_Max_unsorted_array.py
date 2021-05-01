def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 2:
        return None

    min_val = ints[0]
    max_val = ints[0]

    for num in ints:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return (min_val, max_val)



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [ 9,1,0,3,7,4,5]
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


#: test with negative numbers
l = [ 0, 3, 10, 9, -8, 10]
print ("Pass" if ((-8, 10) == get_min_max(l)) else "Fail")

#: test with empty list
l = []
print ("Pass" if (None == get_min_max(l)) else "Fail")

