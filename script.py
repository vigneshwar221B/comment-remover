import re
import sys

def del_comments(file_name):
    new_str = ""
    # to remove the single line comments
    with open(file_name,'r') as f:
        new_str = re.sub('(?<!\")(\/\/[\s\S]*?[\s])(?!\")', '', f.read(), flags=re.S)
    with open(file_name, 'w') as f:
        f.write(new_str)
    # to remove the multi line comments
    with open(file_name, 'r') as f:
        new_str = re.sub('(?<!\")(\/\*[\s\S]*?\/)(?!\")', '', f.read(), flags=re.S)
    with open(file_name, 'w') as f:
        f.write(new_str)

if len(sys.argv)>1:
   
    for filename in sys.argv[1:]:
        del_comments(filename)
else:
    
    name = input("enter the filename: ")
    del_comments(name)