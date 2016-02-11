import os
import shutil

__author__ = 'thornview'

print('-------------------------------------------------')
print('-   FILE SYNC:  Copies local files to remote    -')
print('-------------------------------------------------')

# ===== SET PARAMETERS ===============================
local_dir = "c:\\Users\\embryb\\Documents\\test\\local"
remote_dir = "c:\\Users\\embryb\\Documents\\test\\remote"
local_files = []
remote_files = []

# ===== WALK FILE SYSTEM ==========================
# get list of files in local computer
print('Local files: ')
for root, subdirs, files in os.walk(local_dir):
    for file in files:
        local_files.append(file)
        print(file)

# get list of files on portable device
print('Remote Files: ')
for root, subdirs, files in os.walk(remote_dir):
    for file in files:
        remote_files.append(file)
        print(file)

# generate list of files missing from portable
remote_missing_files = [m for m in local_files if m not in remote_files]
for mfile in remote_missing_files:
    print(mfile)

# copy files from local to portable
for missing_file in remote_missing_files:
    shutil.copy(os.path.join(local_dir, missing_file), remote_dir)
