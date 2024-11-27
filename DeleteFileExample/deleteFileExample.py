import os
import shutil # for deleting a directory

# os.remove('copy.txt')

path = "copy.txt"

try:
    # os.remove(path) # delete a file
    # os.rmdir(path) # delete an empty directory
    # shutil.rmtree(path) # delete a directory and all files contained
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")