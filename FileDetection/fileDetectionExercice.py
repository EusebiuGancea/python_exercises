# Python file detection

import os # operating system

file_path = "test.txt"
# file_path = "C:\\Users\\gancea\\Desktop\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")