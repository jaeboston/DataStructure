def quick_sort(arr, start_i, end_i):

    #: base case
    if start_i >= end_i:
        return arr

    pivot_i = partition(arr, start_i, end_i) #: pivot found its place
    quick_sort(arr,start_i, pivot_i-1)
    quick_sort(arr,pivot_i+1,end_i)

    return arr

def partition(arr, start_i, end_i):

    pivot_i = end_i
    pivot = arr[pivot_i]

    while start_i < pivot_i:
        
        if arr[start_i] < pivot:
            arr[pivot_i] = arr[start_i]
            arr[start_i] = arr[pivot_i-1]
            arr[pivot_i-1] = pivot
            pivot_i = pivot_i-1

        else:
            start_i +=1

    return pivot_i

def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #: Quick Sort
    arr = quick_sort(arr, 0, len(arr)-1)

    #: crate two buckets depending on the size of array
    #: if the len of array is even, two bucket lengths are same
    #: if the len of array is odd, add one to the first bucket

    num1 = ''
    num2 = ''

    i = 0
    while i < len(arr):    
        num1 += str(arr[i])
        i += 1
        if i < len(arr):
            num2 += str(arr[i])
            i += 1
    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
#: edge case
test_function([[4, 4, 4, 4, 4, 4], [444, 444]])
test_function([[9, 2, 0, 0, 1, 1], [910, 210]])
