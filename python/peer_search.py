import os
"""
This script searches through the a directory of files,
looking for text matches, and recording the names of files
with matching text.  It is coded for the PEER project
but can be easily modified.
"""

print('=============================================')
print('=             PROJECT SEARCH                =')
print('=============================================')

# ===== DEFINE FUNCTIONS =============================


def find_string(file_name):
    f = open(file_name, 'r', encoding='utf8')
    search_file = f.read()
    f.close()
    return search_string in search_file.lower()

# ===== SET PARAMETERS ===============================
dirToIgnore = ['.git', '.idea', 'vendor', 'temp', 'images']
fileExtensions = ['.css', '.php', '.phtml', '.js', '.html']

peerDir = 'c:\\Users\\embryb\\Documents\\WebDevelopment\\peer'
subDir = input('Peer Directory (leave blank to search all): ')
searchDir = peerDir + subDir

search_string = input('Search String: ').lower()

output_to_file = input('Save output to file? (Y / N): ').upper()
if output_to_file == 'Y':
    save_file = "results\\" + input('Filename: ')
    files_found = []

# ===== WALK FILE SYSTEM ==========================
for root, subdirs, files in os.walk(searchDir):
    # omit the directories in the "ignore" list
    subdirs[:] = [d for d in subdirs if d not in dirToIgnore]
    # omit file types not in the fileExtension list
    files[:] = [f for f in files if os.path.splitext(f)[1] in fileExtensions]
    for file in files:
        full_file_name = os.path.join(root, file)
        if find_string(full_file_name):
            print(full_file_name)
            if output_to_file == 'Y':
                files_found.append(full_file_name)

# ===== SAVE TO FILE ===========================
if output_to_file == 'Y':
    with open(save_file, mode='wt', encoding='utf-8') as out_file:
        out_file.write("\n".join(files_found))