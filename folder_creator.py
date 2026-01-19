import os

a = int(input("How many folders do you want from 1 to: "))
b = input("What will be the name (e.g., Day, Project, etc.)? ")

def folder_creator(a, b):
    for i in range(a):
        folder_name = f"{b} {i}"
        os.mkdir(folder_name)
        print(f"Created folder: {folder_name}")

def folder_deletor(a, b):
    for i in range(a):
        folder_name = f"{b} {i}"
        try:
            os.rmdir(folder_name)
            print(f"Deleted folder: {folder_name}")
        except OSError as e:
            print(f"Could not delete {folder_name}: {e}")

folder_creator(a, b)   
