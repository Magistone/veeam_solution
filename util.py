import hashlib
from os import walk

def create_folder_hash_disctionary(dir: str):
    #dir = '/home/magistone/screecher'
    file_dict = dict()
    dir_list = set()
    for root, dirs, files in walk(dir):
        #print(f"ROOT: {root}")
        #print(f"DIR: {dir}")
        relative_prep = root.replace(dir, "")
        if relative_prep.startswith('/'):
            relative_prep = relative_prep[1:]
        #print(f"RELATIVE: {relative_prep}")
        #print(relative_prep)

        #Create Hash File Dictionary
        for file in files:
            relative_file = relativeName(relative_prep, file)
            file_dict[relative_file] = hashFile(root, file)
        
        #Create List of Dirs
        for local_dir in dirs:
            relative_dir = relativeName(relative_prep, local_dir)
            dir_list.add(relative_dir)
    #print(dir_list)
    return (file_dict, dir_list)


def hashFile(root: str, file: str):
    opened = open(root+"/"+file, "rb")
    file_contents = opened.read()

    hash = hashlib.md5(file_contents)
    return hash.hexdigest()

def relativeName(relative_prep: str, obj: str):
    #print(relative_prep)
    #print(obj)
    if relative_prep != "":
        relative_obj = relative_prep + "/" + obj
    else:
        relative_obj = obj
    
    #print(relative_obj)
    return relative_obj