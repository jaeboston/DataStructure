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

    Note that a path may contain further subdirectories and those
    subdirectories may also contain further subdirectries.

    There are no limit to the depth of the subdirectories can be

    Args:
        suffix(str): suffix if the file name ot be found
        path(str): path of the file system

    Returns:
        a list of paths
    """

    obj_list = os.listdir(path)
    
    if len(obj_list) == 0:
        return

    for obj in obj_list:
        if os.path.isdir(path + '/' + obj):
            find_files(suffix, path + '/' + obj)

        else:
            if obj.endswith(suffix):
                print(path + '/' + obj)

    return

#: TEST CASES

find_files('.c', './P1_DataStructure')

find_files('.d', './P1_DataStructure')

find_files('.cd', './P1_DataStructure')
