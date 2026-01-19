import os
a = int(input("How many file do you want from 1 to : ")
b = input("What will be the name ex:Day ,Project etc .. : "
def folder_creator(a,b):
    for i in range(a):
        os.mkdir(f"b {i}")

def folder_deletor(a,b):
    for i in range(a):
        os.rmdir(f"b {i}")

folder_creator(a,b)
  
