import util

(in_folder, in_folder_list) = util.create_folder_hash_disctionary('/home/magistone/in')
(out_folder, out_folder_list)  = util.create_folder_hash_disctionary('/home/magistone/out')

print(in_folder_list)
print(out_folder_list)

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
print(f"TO BE COPIED: {in_folder.keys()}")
print(f"TO BE DELETED: {out_folder.keys()}")
print(f"MATCHED, do nothing: {matched}")
print(f"OVERWRITE: {overwrite}")

to_delete = out_folder_list - in_folder_list
print("----DIRS----")
print(f"DANGLING FOLDERS TO DELETE: {to_delete}")