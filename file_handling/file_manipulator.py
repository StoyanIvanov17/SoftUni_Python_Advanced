import os


def add(item):
    content = command[2]
    with open(file_name, "a") as file:
        file.write(f"{content}\n")


def replace(item):
    old_string, new_string = command[2], command[3]

    try:
        with open(file_name, "r") as input_file:
            text = input_file.read()

        text = text.replace(old_string, new_string)

        with open(file_name, "w") as output_file:
            output_file.write(text)

    except FileNotFoundError:
        print('An error occurred')


def delete(item):
    try:
        os.remove(file_name)

    except FileNotFoundError:
        print('An error occurred')


while True:
    command = input().split('-')
    action = command[0]

    if action == "End":
        break

    file_name = command[1]

    if action == "Create":
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        add(file_name)

    elif action == "Replace":
        replace(file_name)

    elif action == "Delet":
        delete(file_name)
        
