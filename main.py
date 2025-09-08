from colorama import Fore, Back, Style
import os

cached_list = []

# "cls" for NT Windows
# "clear" for POSIX
CLEAR_COMMAND = "clear"

with open("cache", "r") as cache:
    cache = cache.readlines()
    for line in cache:
        cached_list.append(line.strip())

user_input = input("""
1. Add item
2. Show all
3. Update item
4. Remove item
5. Grep list
6. Quit
""")

def menu():
    if user_input == "1":
        os.system(f"{CLEAR_COMMAND}")
        print()
        ask_add_item()
    elif user_input == "2":
        os.system(f"{CLEAR_COMMAND}")
        print()
        print(cached_list)
    elif user_input == "3":
        os.system(f"{CLEAR_COMMAND}")
        print()
        ask_update_item()
    elif user_input == "4":
        os.system(f"{CLEAR_COMMAND}")
        print()
        ask_remove()
    elif user_input == "5":
        os.system(f"{CLEAR_COMMAND}")
        print()
        grep()
    elif user_input == "6":
        return
    # This is my error handling for menu()
    else:
        print("Please run the script again and input a valid number corresponding to an action listed!")



def ask_add_item():
    cached_list.append(input("type item to add: "))
    print("item added")

def ask_update_item():
    for i, elem in enumerate(cached_list):
        print(f"{i} {elem}")
    index = int(input("please input index to update: "))
    cached_list[index] = input("input new value: ") 
    print(cached_list)

def ask_remove():
    for i, elem in enumerate(cached_list):
        print(f"{i} {elem}")
    index = int(input("please input index to remove: "))
    del cached_list[index]
    print(cached_list)

def grep():
    query = input("Input search string: ")
    print()
    try:
        for i, line in enumerate(cached_list):
            if line == cached_list[cached_list.index(query)]:
                print(Fore.RED + line)
            else:
                print(Fore.WHITE + line)
    except:
        print(f"{query} not found in cache")

menu()

with open("cache", "w") as f:
    for item in cached_list:
        f.write(f"{item}\n")

#TODO: Show menu again after making a choice
#TODO: Type string (dumb fuzzy, show ambiguous if not enough) or input index to remove
