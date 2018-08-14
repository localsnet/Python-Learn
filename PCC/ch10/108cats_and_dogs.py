
filenames = ['cats.txt', 'dogs.txt']
# 1. Read each file
for filename in filenames:
# 3. Wrap code to catch the FileNotFound error
    try:
        with open(filename) as f_obj:
         contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
# 2. Print content of each file to the screen
    print(contents.rstrip())



