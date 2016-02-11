import os

"""
Tag scraper currently finds the first instance of a tag set in a file,
then returns the stuff between those tags.  Needs to be updated
to handle multiple instances in a file, but I don't need that today.
"""

print('=============================================')
print('=         <tag> scraper                     =')
print('=============================================')
print()

# ===== DEFINE FUNCTIONS =============================


def get_text_in_file(file_name):
    f = open(file_name, 'r', encoding='utf8')
    search_file = f.read()
    f.close()
    return search_file.lower()


def has_tags(ht_text, ht_tag1, ht_tag2):
    return ht_tag1 in ht_text and ht_tag2 in ht_text


def find_second_tag(st_text, st_tag2):
    """
    :param st_text:
    :param st_tag2:
    :return: int - index of first character BEFORE the tag
    """
    return st_text.find(st_tag2)


def find_first_tag(ft_text, ft_tag1):
    """
    :param ft_text:
    :param ft_tag1:
    :return: int - index of first character AFTER the tag
    """
    return ft_text.find(ft_tag1) + len(ft_tag1)


def get_text_between_tags(tbt_text, tbt_start_tag, tbt_end_tag):
    tbt_start = find_first_tag(tbt_text, tbt_start_tag)
    tbt_end = find_second_tag(tbt_text, tbt_end_tag)
    return tbt_text[tbt_start:tbt_end]


# ===== SET PARAMETERS ===============================
dirToIgnore = ['.git', '.idea', 'vendor', 'temp', 'images', 'style']
fileExtensions = ['.css', '.php', '.phtml', '.js', '.html']

peerDir = 'c:\\Users\\embryb\\Documents\\WebDevelopment\\peer'
subDir = input('Peer Directory (leave blank to search all): ')
searchDir = peerDir + subDir

start_tag = input('Start tag: ').lower()
end_tag = input('End tag: ').lower()

output_to_file = input('Save output to file? (Y / N): ').upper()
if output_to_file == 'Y':
    save_file = "results\\" + input('Filename: ')
    results = []

# ===== WALK FILE SYSTEM ==========================
for root, subdirs, files in os.walk(searchDir):

    # omit the directories in the "ignore" list
    subdirs[:] = [d for d in subdirs if d not in dirToIgnore]

    # omit file types not in the fileExtension list
    files[:] = [f for f in files if os.path.splitext(f)[1] in fileExtensions]

    for file in files:
        full_file_name = os.path.join(root, file)
        text = get_text_in_file(full_file_name)
        if has_tags(text, start_tag, end_tag):
            tag_text = get_text_between_tags(text, start_tag, end_tag)
            counter = text.count(start_tag)
            summary = "/* Found: " + str(counter) + " in: " + full_file_name + " */"
            print(summary)
            print(tag_text)
            if output_to_file == 'Y':
                results.append(summary)
                results.append(tag_text)

# ===== SAVE TO FILE ===========================
if output_to_file == 'Y':
    with open(save_file, mode='wt', encoding='utf-8') as out_file:
        out_file.write("\n".join(results))
