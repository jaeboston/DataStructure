# Objective: 
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1.

# Constraint: 
- Time Complexity: O(NlogN)
- You're not allowed to use any sorting function that Python provides


# Algorithm 

- input: `INPUT_ARRAY` (array type)

Use a sorting alrogithm to sort the input array. We can choose the Quick Sort algorithm which has O(NlogN) time complexity on average and very efficient space complexcity of O(1).
Once, the input is sorted, then we can initialize two strings.

Iterate thru each element from the largest to the smallest in the input array, assign it to each of two strings we created eariler alternatively.

Convert those two strings to intergers and return them as a list.


The time complexity of this algorithm would be O(NlogN). The space complexity would be O(N)