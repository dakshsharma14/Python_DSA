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

# save_our_data()
def read_user_data():
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return

    with open('user_data.json', 'r')as file:
        user_list = json.load(file)
        for user_data in user_list:
            print("Name: ", user_data["name"])
            print("E-mail: ", user_data["email:"])
            print("Contact: ", user_data["contact"])
            print("\n")
# read_user_data()

def edit_user_data(name):
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return

    with open('user_data.json', 'r') as file:
        user_list = json.load(file)

        user_found = False
        for user_data in user_list:
            if user_data['name'].lower() == name.lower():
                email = input("Enter updated email: ")
                contact = input("Enter updated contact: ")

                user_data["email:"] = email
                user_data["contact"] = contact
                user_found = True
                break
        if not user_found:
            print("User not found")

    with open("user_data.json", 'w') as file:
        json.dump(user_list,file)
    print("User data updated successfully")


edit_name = input('Enter a name which you want to edit data for: ')
edit_user_data(edit_name)
read_user_data()