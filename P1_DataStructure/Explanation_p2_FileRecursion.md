Using recursion methid, each time we see a sub-folder, we execute the method recursively.
The base case for the recusion is if the path is a file.
Then, we see a file with the suffix, we simply add the file with path to the output list.

The time complexity would be O(n) where n is the number items in the folder. Itmes includes sub-folders and files.
This is because we visit every single items in the top folder once.

The space complexity would be O(N) where N is all objects including files and directories.


