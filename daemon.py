import util
import io
import datetime 
import shutil

class Synchronizer:
    src: str
    dst: str
    log_file: io.TextIOWrapper

    def __init__(self, src: str, dst: str, log_file: io.TextIOWrapper):
        self.src = src
        self.dst = dst
        self.log_file = log_file

    def sync(self):
        src = '/home/magistone/in'
        dst = '/home/magistone/out'
        (in_folder, in_folder_list) = util.create_folder_hash_disctionary(src)
        (out_folder, out_folder_list)  = util.create_folder_hash_disctionary(dst)

        #print(in_folder_list)
        #print(out_folder_list)

        matched = list()
        overwrite = list()

        keys = list(in_folder.keys())

        for k in keys:
            if(out_folder.get(k)):
                #File exists in out, must check hash
                if (out_folder.get(k) == in_folder.get(k)):
                    #MATCH
                    matched.append(k)    
                else:
                    # Must overwrite, different version
                    overwrite.append(k)
                del out_folder[k]
                del in_folder[k]
            else:
                #File does not exists in out, must copy
                pass
        print("----FILES----")
        print(f"TO BE COPIED: {in_folder.keys()}") #Copy
        print(f"TO BE DELETED: {out_folder.keys()}") #Delete
        print(f"MATCHED, do nothing: {matched}") #Do Nothing
        print(f"OVERWRITE: {overwrite}") #Copy

        to_delete = out_folder_list - in_folder_list
        print("----DIRS----")
        print(f"DANGLING FOLDERS TO DELETE: {to_delete}") #Delete

        self.do_deletes(list(out_folder.keys()), to_delete)
        self.do_copies

    def do_deletes(self, files: list[str], folders: list[str]):
        for file in files:
            #delete file
            #write log
            pass
        for folder in folders:
            #delete folder
            #write log
            pass
    
    def do_copies(self, files: list[str]):
        for file in files:
            #copy file
            #write log
            pass

    def do_already_synced(self, files: list[str]):
        for file in files:
            #write log
            pass
    
    def log(self, op: str, path: str):
        now = datetime.datetime.strftime(datetime.datetime.now(), "%b %d, %Y %H:%M:%S")
        msg = f"{now} - {op} {path}\n"
        print(msg)
        self.log_file.write(msg)
