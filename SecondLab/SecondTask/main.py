from container import *
import re
def check_input():
    username = input("Enter username: ")
    while not re.findall(r'\b[A-z]+\b', username):
        print("Incrorect name")
        username = input("Enter username: ")
    return username


storage = UserStorage()
while True:
    username = check_input()

    user_container = storage.switch_user(username)

    while True:
        command = input("Enter command: ")
        match command:
            case "add":
                keys = input("Enter keys separated by space: ").split()
                user_container.add(*keys)
            case "remove":
                key = input("Enter key to remove: ")
                user_container.remove(key)
            case "find":
                keys = input("Enter keys separated by space: ").split()
                user_container.find(*keys)
            case "show":
                user_container.show()
            case "grep":
                regex = input("Enter regular expression: ")
                user_container.grep(regex)
            case "save":
                user_container.save()
            case "load":
                user_container.load()
            case "switch":
                break
            case "exit":
                storage.save_all()
                print("Exiting...")
                exit(0)
            case _:
                print("Invalid command, try again")