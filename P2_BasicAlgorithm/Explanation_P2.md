# Objective: 
You are given a target value to search. If found in the array return its index, otherwise return -1. The array is sorted and rotated at some random pivot point.

# Constraint: 
Time Complexity: O(logN)

# Algorithm 
* input: `INPUT_ARRAY` (array type), `TARGET` (integer)

We can create two helper functions. One is to find the rotation index of the input array. The second is to find the index of target in the input array. Both of two helper functions use the binary search concept recursively to speed up the search.

First, we call the helper function, `find_rotation_index` recursively to find the index.
Once we find the roation index we can split the input array into two arrays using the rotation index.
Check the target with the first index value of the input array, if the target is smaller then use the first half of the input array to find the target. To find the target, we can use the second helper function, `binary_search` recursively to find the index.

The time complexity of this algorithm would be O(logN). The space complexity would be O(1)
