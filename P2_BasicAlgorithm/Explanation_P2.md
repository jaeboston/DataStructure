# Objective: 
You are given a target value to search. If found in the array return its index, otherwise return -1. The array is sorted and rotated at some random pivot point.

# Constraint: 
Time Complexity: O(logN)

# Algorithm 
* input: `INPUT_ARRAY` (array type), `TARGET` (integer)

To meet the time complexity constraint, we use the binary search concept. The array contains a pivot point so we need to modify the bianry search to check for the pivot point.

We create a helper function which is called recursively with the begin and end index defining the array size.
Like the binary search, we check the mid point array value and wheather there is a pivot point or not.
To check the existance of a pivot point, we check the beging index value and the mid index value.
If the mid index value is less than the begin index value, we know there is a pivot point between the begin and mid.
There would be two base cases for this recursive fuction.
1st Base case: when the begin and end index is the same and the begin value is not the target, then we return -1
2nd Base case: when the being value equals the target, we return the begin index.


We start off by comparing `TARGET`  with the begin.
If `TARGET` is greater then the begin, we determin wheather there is a pivot between the begin and the mid.

## CASE : `TARGET` > the begin and there is a pivot between the begin and the mid
* We compare `TARGET` with the mid. If `TARGET` is greater than the mid, we know `TARGET` exist between the begin and the mid because of the pivot. So we recursively call the helper function setting the begin index as it is and the end index as the mid-1 point 

* If `TARGET` equals the mid, we simply return the mid index.

* If `TARGET` is less than the mid, we know `TARGET` exists between the mid and the end. So we recursively call the helper fuction
setting the begin index as it is and the end index as the mid index -1

## CASE : `TARGET` > the begin and there is NOT a pivot between the begin and the mid
* Just like the binary search, if `TARGET` is greater than the mid, we know the target exist between the mid and the end. So we recursively call the helper function setting the begin index and the mid+1 point and the end as the end 
