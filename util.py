import hashlib
from os import walk

def create_folder_hash_disctionary(dir: str):
    """ 
    Creates hash for all files contained in the directory. 

    Arguments:
        dir: the directory of which to hash all files

    Returns: tuple(dict, set)
        dict: Contains hash for each file in the directory. The key is relative path to 'dir'
        set: Contains all directories relative to 'dir' excluding 'dir'
    """

    file_dict = dict()
    dir_list = set()
    for root, dirs, files in walk(dir):
        relative_prep = root.replace(dir, "")
        if relative_prep.startswith('/'):
            relative_prep = relative_prep[1:]

        #Create Hash File Dictionary
        for file in files:
            relative_file = relativeName(relative_prep, file)
            file_dict[relative_file] = hashFile(root, file)
        
        #Create List of Dirs
        for local_dir in dirs:
            relative_dir = relativeName(relative_prep, local_dir)
            dir_list.add(relative_dir)
        
    return (file_dict, dir_list)


def hashFile(root: str, file: str):
    """ Creates hash of a file """
    opened = open(root+"/"+file, "rb")
    file_contents = opened.read()

    hash = hashlib.sha256(file_contents)
    return hash.hexdigest()

def relativeName(relative_prep: str, obj: str):
    """ Creates relative path to root """
    if relative_prep != "":
        relative_obj = relative_prep + "/" + obj
    else:
        relative_obj = obj

    return relative_obj