def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """


    #: find the rotation point first
    rot_i = find_rotation_index(0, len(input_list)-1, input_list)
    
    #: edge case when rot_i == -1
    if rot_i == -1:
        #: check the edge case for max number
        if number > input_list[-1]:
            return -1
        #: use the whole array
        output = binary_search(0, len(input_list)-1, input_list, number)
    
    #: rot_i >= 0
    else:
        #: determine with part of the list to use for the serach
        if number < input_list[0]:
            #: check the edge case for max number
            if number > input_list[-1]:
                return -1
            #: use the second half
            output = binary_search(rot_i, len(input_list)-1, input_list, number)
        else:
            #: check the edge case for max number
            if number > input_list[rot_i-1]:
                return -1
            #: use the first half
            output = binary_search(0, rot_i, input_list, number)
            
    return output

            
def binary_search(start_i, end_i, nums, num):
    """
    Find the index by searching in a sorted array

    Args:
       start_i(int), end_i : start index and end index of the input array
       nums(array), numb(int): Input array to search and the target
    Returns:
       int: Index or -1
    """


    mid_i = start_i + (end_i - start_i)//2
    
    if num == nums[mid_i]:
        return mid_i
    elif num > nums[mid_i]:
        return binary_search(mid_i+1, end_i, nums, num)
    else:
        return binary_search(start_i, mid_i-1, nums, num)
    

def find_rotation_index(start_i, end_i, nums):
    """
    Find the rotation index

    Args:
       start_i(int), end_i : start index and end index of the input array
       nums(array): Input array to search
    Returns:
       int: Index or -1
    """
    #: base case
    if end_i - start_i == 1 :
        if nums[end_i]< nums[start_i] :
            return end_i
        else:
            return -1
    
    mid_i = start_i + (end_i - start_i)//2
    if nums[mid_i] < nums[0]: #: rotation happened before mid
        return find_rotation_index(start_i, mid_i, nums)
        
    else:
        return find_rotation_index(mid_i, end_i, nums)
    
    return -1

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

#: test edge case: no rotation index
test_function([[6, 7, 8, 9, 10, 11, 12], 10])
#: test edge case: target not found 
test_function([[6, 7, 8, 1, 2, 3, 4], 5])



