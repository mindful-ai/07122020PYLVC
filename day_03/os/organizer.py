import os
import os.path
import shutil

path = r""

os.chdir(path)

files = os.listdir()
exts = []
for file in files:
    exts.append(os.path.splitext(file)[1][1:])

for ext in set(exts):
	os.mkdir(ext)

for file in files:
	newdir = os.path.splitext(file)[1][1:]
	dest = os.path.join(os.getcwd(), newdir, file)
	shutil.move(file, dest)