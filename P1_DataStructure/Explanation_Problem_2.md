Using recursion methid, each time we see a sub-folder, we execute the method recursively.
The base case for the recusion is if the sub-folder contains no item. (empty folder)
Once we see a file with the suffix, we simply print the file path

The time complexity would be O(n) where n is the number items in the folder. Itmes includes sub-folders and files.
This is because we visit every single items in the top folder once.



