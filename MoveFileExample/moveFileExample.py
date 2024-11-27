import os

# file
source = "output.txt"
destination = "C:\\Users\\gance\\Desktop\\output.txt"

# folder

# source = "folder
# destination = "C:\\Users\\gance\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

