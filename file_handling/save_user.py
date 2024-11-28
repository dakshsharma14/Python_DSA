while True:
    with open('name.txt', 'a') as file:
        name = input("Enter name to be added: ")
        file.write(name + '\n')
        choice = input("Do you want to continue y/n: ")
        if choice == 'n':
            break
