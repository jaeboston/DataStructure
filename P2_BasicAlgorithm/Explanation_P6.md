# Objective: 
we will look for smallest and largest integer from a list of unsorted integers. 
# Constraint: 
- The code should run in O(n) time. 
- Do not use Python's inbuilt functions to find min and max.


# Algorithm 

We comapre the first two elements input array and assign them as min_val and max_val variables.
Starting the thrid element, compare it to the min_val and max_val and replace those variables accordingly.
Return min_val, max_val as a Tuple.
