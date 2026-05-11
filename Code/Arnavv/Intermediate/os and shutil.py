import os
import shutil

# For current working directory

cwd = os.getcwd()
print(f"The current working directory is {cwd}")

# to change working directory
os.chdir(r"C:\Users\Students\Desktop\Arnavv\Intermediate")

cwd = os.getcwd()
print(f"The current working directory is {cwd}")

# List directories

lsdir = os.listdir()
print(lsdir)


# Remove file and directories
filename = "example.txt"
os.remove(filename)

dirname = 'aaa'
os.rmdir(dirname)


# renaming files

os.rename('test.json', 'test1.json')    