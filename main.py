# saved_list = ["what", "test", "conf"]
cached_list = []
local_changes = []

#INFO: 2025-09-04 stopped at realizing my local_chages thing breaks due to the fact of removing items

with open("cache", "r") as cache:
    cache = cache.readlines()
    for line in cache:
        print(line, sep="", end="")
        #INFO: No idea what more it strips
        cached_list.append(line.strip())

def writeCache(*args):
    with open("cache", "a") as cache:
        for arg in args:
            print(arg, sep="", end="")
            cache.write(f"{arg}\n")

user_input = input("""
1. Add item
2. Show all
3. Update item
4. Remove item
5. Quit
""")

def menu():
    if user_input == "1":
        ask_add_item()
    elif user_input == "2":
        print(cached_list)
    elif user_input == "3":
        ask_update_item()
    elif user_input == "4":
        ask_remove()
    elif user_input == "5":
        return

def ask_add_item():
    local_changes.append(input("type item to add"))
    writeCache(input("type item to add"))
    print("item added")

def ask_update_item():
    for i, elem in enumerate(cached_list):
        print(f"{i} {elem}")
    index = int(input("please input index to update"))
    cached_list[index] = input("input new value") 
    print(cached_list)

def ask_remove():
    for i, elem in enumerate(cached_list):
        print(f"{i} {elem}")
    index = int(input("please input index to remove"))
    del cached_list[index]
    print(cached_list)

#FIX: Implement error handling

menu()

#FIX: just duplicates everything
# with open("cache", "a") as f:
#     for item in cached_list:
#         f.write(f"{item}\n")
