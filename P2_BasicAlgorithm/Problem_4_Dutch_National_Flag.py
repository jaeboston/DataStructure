def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    output_list = [1 for _ in range(len(input_list)) ]
    
    idx0 = 0
    idx2 = len(input_list)-1
    for i in range(len(input_list)):
        if input_list[i] == 0:
            output_list[idx0] = 0
            idx0 +=1
        if input_list[i] == 2:
            output_list[idx2] = 2
            idx2 -=1
    
    return output_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

#: edge cases
test_function([0, 0, 0, 0, 0])
test_function([0, 0, 0, 0, 2])
