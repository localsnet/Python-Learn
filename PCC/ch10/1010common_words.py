#!/usr/bin/python3

filenames = ['1056.txt.utf-8']
# 1. Read each file
for filename in filenames:
# 3. Wrap code to catch the FileNotFound error
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
#to fail silently if either file is missing
     pass
# 2. Print content of each file to the screen
    else:
        print('in file '+ filename + ' "the" contains: ')
        print('Lower cases only: '+ str(contents.count('the')))
        print('All cases: '+ str(contents.lower().count('the')))