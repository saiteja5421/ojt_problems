import shutil
import os

# # path to source directory
src_dir = 'dir3'

# path to destination directory
dest_dir = 'dir2'
# getting all the files in the source directory
files = os.listdir(src_dir)
print(files)
shutil.copytree(src_dir, dest_dir)
shutil.rmtree('dir3')

# import re
# text, pattern = input(), input()
# m= list(re.finditer("(?=(%s))"%pattern,text))
# if not m:
#     print((-1,-1))
# for i in m:
#     print((i.start(1),i.end(1)-1))
