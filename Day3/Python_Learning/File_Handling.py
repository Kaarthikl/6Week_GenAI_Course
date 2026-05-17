import os

print(os.getcwd())
print(os.listdir())
#os.mkdir("test_folder")
file = open("notes.txt","r")
content = file.read()
print(content)
file = open("notes.txt","w")
file.write("content changed")
file.close()
file = open("notes.txt","a")
file.write("\ncontent added newly\n")
file.close()

from test_folder.package import add
result = add(7,10)
print(result)