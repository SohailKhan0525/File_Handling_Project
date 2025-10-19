from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the file you want to create: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter what you want to write: ")
                fs.write(data)
            print("***************************")
            print("File created successfully..")
            print("***************************")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("This file already exists.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the file you want to read: ")
        p = Path(name)
        if p.exists and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("-------------------------")
                print(data)
                print("-------------------------")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("This file doesn't exists.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the file you want to delete: ")
        p = Path(name)
        if p.exists and p.is_file():
            os.remove(name)
            print("**************************")
            print("File deleted successfully.")
            print("**************************")
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("This file doesn't exists.")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    except Exception as err:
        print(f"An error occured as {err}")

while True:
    print("**************************")
    print("Press '1' to create a file")
    print("Press '2' to read a file")
    print("Press '3' to delete a file")
    print("Press '4' to quit the program")
    print("**************************")

    try:
        check = int(input("Enter your response: "))
    except Exception as error:
        print(f"Please enter a valid number [{error}]")
    if check == 1:
        createfile()
    elif check == 2:
        readfile()
    elif check == 3:
        deletefile()
    elif check == 4:
        print("----------------------")
        print("Quitting.... Good Bye!")
        print("----------------------")
        break
    else:
        print(f"{check} is a/an invalid.")
        