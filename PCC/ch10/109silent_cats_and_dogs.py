
filenames = ['cats.txt', 'dogs.txt']
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
        print(contents.rstrip())