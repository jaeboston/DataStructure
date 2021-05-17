#: goal: finding all files under a directory (and all directories beneath it) that end wth '.c'
#: use the following resources
#: os.path.isdir(path)
#: os.path.isfile(path)
#: os.listdir(directory)
#: os.path.join(...)


import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []
    helper(suffix, path, output)
    return output

def helper(suffix, path, output):

    if os.path.isfile(path):
        if path.endswith(suffix):
            output.append(path)
            return
    else: 
        obj_list = os.listdir(path)

        for obj in obj_list:
            new_path = path + '/' + obj
            helper(suffix, new_path, output)


#: TEST CASES

print(find_files('.c', './P1_DataStructure'))

print(find_files('.d', './P1_DataStructure'))

print(find_files('.cd', './P1_DataStructure'))

