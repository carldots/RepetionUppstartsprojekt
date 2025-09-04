# my_list = ["what", "test", "conf"]
my_list = []

with open("cache", "r") as cache:
    cache = cache.readlines()
    for line in cache:
        print(line, sep="", end="")
        #INFO: No idea what more it strips
        my_list.append(line.strip())

user_input = input("""
1. Add item
2. Show all
3. Update item
4. Remove item
5. Quit
""")

#FIX: make functions for repititions

def menu():
    if user_input == "1":
        my_list.append(input("type item to add"))
        print("item added")
    elif user_input == "2":
        print(my_list)
    elif user_input == "3":
        for i, elem in enumerate(my_list):
            print(f"{i} {elem}")
        index = int(input("please input index to update"))
        my_list[index] = input("input new value") 
        print(my_list)
    elif user_input == "4":
        for i, elem in enumerate(my_list):
            print(f"{i} {elem}")
        index = int(input("please input index to remove"))
        del my_list[index]
        print(my_list)
    elif user_input == "5":
        return

def ask_add_item():
    my_list.append(input("type item to add"))
    print("item added")

def show_all():
    print(my_list)

def ask_update_item():
    for i, elem in enumerate(my_list):
        print(f"{i} {elem}")
    index = int(input("please input index to update"))
    my_list[index] = input("input new value") 
    print(my_list)

def ask_remove():
    for i, elem in enumerate(my_list):
        print(f"{i} {elem}")
    index = int(input("please input index to remove"))
    del my_list[index]
    print(my_list)

#FIX: Implement error handling

menu()

with open("cache", "a") as f:
    for item in my_list:
        f.write(item)
