First, we check the `group` object's `users` array property and if the array has at least one user, we check to see if the passed in `username` exists in the array. If exists we return True. Otherwise, we iterate each sub group in the `groups` array property.
In each iteration, we call the `is_user_in_group` function passing in the `username` originally passed in and the sub group recursively. Using Depth First Seach (DFS), we can go into the deepest path available for all the sub groups in the `groups` array to find the username.

The complexity would be O(N*M) where N is the number of all sub groups and M is the maximum number of `usernames` in all sub gruops.
 
The space complexity would be O(N) where N is all objects including groups and users.