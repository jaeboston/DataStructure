# Objective: 
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.


# Constraint: 
- Single traversal of the input array

# Algorithm 

- input: `INPUT_ARRAY` (array type)

Create a output array same size as the input array. Be default all elements in the output array is 1.
Create two index variables for where to place 0 and 2. For 0, start at 0 and for 2, start at len(INPUT_ARRAY)-1
Iterate each element in the input array, if an element is 1 skip to next one. If 1, use the index for 0 to place 0 on the output array. If 2, use the index for 2 to place 2 on the output array.
Return the output array.

The time complexity of this algorithm would be O(N). The space complexity would be O(N) as well.