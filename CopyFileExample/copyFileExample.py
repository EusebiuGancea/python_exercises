# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies medadata (file's creation and modification times)

import shutil

shutil.copyfile('output.txt','copy.txt') #src,dest

# shutil.copyfile('output.txt','C:\\Users\\gancea\\Desktop\\copy.txt')