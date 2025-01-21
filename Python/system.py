import os
import time
from os import path
file=open("Untitled.txt","w+")
for i in range(80):
    file.write("Pavithran\n")
file1=open("Untitled.txt","r")
if file.mode=='r':
        contents=file.read()
        print(contents)

print(os.name)
print(path.isfile("Untitled.txt"))
t=time.ctime(path.getmtime("Untitled.txt"))
print(t)