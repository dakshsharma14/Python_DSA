import json
import os

def save_our_data():
    user_list = []

    while True:
        name = input("Enter name (or 'quit to exit the program'): ")
        if name == 'quit':
            break
        email = input("Enter email: ")
        contact = input("Enter contact: ")

        # creating a pythn dict
        user_data= {
            'name': name,
            'email:': email,
            'contact': contact
        }

        user_list.append(user_data)

    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)

    with open('user_data.json','w') as file:
        json.dump(user_list, file)

    print("User data saved successfully")

save_our_data()