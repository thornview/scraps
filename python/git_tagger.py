import git

# Connect to git repo and get the current tag
repo = git.Repo.init("c:/Users/embryb/Documents/Python/toolbox/")
tags = repo.tags
current_tag = tags[-1]

# parse the tag
tag_parts = str(current_tag).split('.')
build = tag_parts[2]
point = tag_parts[1]
main =  tag_parts[0]
print("Current Version: " + str(current_tag))

# ask what portion to update
print("Okay, what are we incrementing today?")
print("    [M]ain:  " + main)
print("    [P]oint:  " + point)
print("    [B]uild:  " + build + "  -- Default")
to_increment = input("    [M], [P], [B] or leave blank for default: ").lower()


if to_increment == 'm':
    new_main = int(main.strip('v')) + 1
    new_tag = "v" + str(new_main) + ".0.0"
elif to_increment == 'p':
    new_point = int(point) + 1
    new_tag = main + "." + str(new_point) + ".0"
else:
    new_build = int(build) + 1
    new_tag = main + "." + point + "." + str(new_build)

repo.create_tag(new_tag)
origin = repo.remote('python_scripts')
origin.push('--tags')

print("New Version: " + new_tag)
