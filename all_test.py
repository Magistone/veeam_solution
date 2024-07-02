import util
import daemon
import shutil

def test_all_files_in_hash_dict():
    (files, dirs) = util.create_folder_hash_disctionary('./test_files/out')
    actual_files = ['somefile', 'pp', 'hello/filez', 'peepee/hi.bin']
    actual_dirs = ['hello', 'peepee', 'peepee/QQ']

    #One way includes
    for dir in dirs:
        assert(dir in actual_dirs)
    
    for file in list(files.keys()):
        assert(file in actual_files)

    #Other way includes for equivalence
    for dir in actual_dirs:
        assert(dir in dirs)
    
    for file in actual_files:
        assert(file in list(files.keys()))


def test_relative_name():
    name = 'file.bin'
    new_name = util.relativeName("", name)

    assert (new_name == name)

    new_name = util.relativeName("/root/karel", name)
    
    assert(new_name == "/root/karel" + "/" + name)

def test_sync():
    in_path = './test_files/in'
    out_path = './test_files/out_test'

    shutil.copytree('./test_files/out', out_path)
    thething = daemon.Synchronizer(in_path, out_path, open('./test_files/log', '+wt'))
    thething.sync()

    in_dist = util.create_folder_hash_disctionary(in_path)
    out_dist = util.create_folder_hash_disctionary(out_path)

    shutil.rmtree(out_path)
    #shutil.rmtree('./test_files/log')
    assert(in_dist == out_dist)
