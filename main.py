my_list = ["what", "test", "conf"]


#FIX: casting whatever read() returns to an actual list since indexing does not work

# with open("cache") as f:
#     global my_list
#     my_list = f.read()
#
# print(my_list, sep="", end="")
# print(my_list[3])

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
    f.write(f"{my_list}")
