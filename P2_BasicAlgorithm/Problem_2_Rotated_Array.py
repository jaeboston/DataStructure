def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    index = search_helper(input_list, number, 0, len(input_list)-1) 
    #print(f'index={index}')
    return index

def search_helper(input, target, beg, end):

    mid = (end-beg)//2 + beg

    #: base case 1
    if beg == end and target != input[beg]:
        return -1

    #: base case 2
    if target == input[beg]:
        return beg

    elif target > input[beg]:

        if input[mid] > input[beg]: #: no pivot between 
            if target > input[mid]:
                return search_helper(input, target, mid+1, end)
            elif target == input[mid]:
                return mid
            else:
                return search_helper(input, target, beg, mid-1)
        
        else: #: there is a pivot between
            if target > input[mid]:
                return search_helper(input, target, beg, mid-1)
            elif target == input[mid]:
                return mid
            else:
                return search_helper(input, target, mid+1, end)

    else: #target < input[beg]

        if target > input[mid]:
            return search_helper(input, target, beg, mid-1)
        
        elif target == input[mid]:
            return mid
        
        else: #target < input[mid]
            return search_helper(input, target, mid+1, end)
        



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])