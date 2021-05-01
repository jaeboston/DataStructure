# Objective: 
we will look for smallest and largest integer from a list of unsorted integers. 
# Constraint: 
- The code should run in O(n) time. 
- Do not use Python's inbuilt functions to find min and max.


# Algorithm 

We create two variables `min_val`,`max_val` to hold min and max val. Then we initilize these variables with the first value in the input array.
Then, we simply iterate thru each item in the input array.
If we find a value that is smaller than `min_val`, update `min_val`.
If we find a value that is larger than `max_val`, update `max_val`.
After the iteration, we can return two variables as Tuple.

The time complexity of this algorithm would be O(N). The space complexity would be O(1)