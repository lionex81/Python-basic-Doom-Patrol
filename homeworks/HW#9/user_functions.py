import json
import os
import logging

def check_email(email, all_users_data):
    for user in all_users_data:
        if email == user['Email']:
            return True
    return False

def create_file():
    if os.path.exists('databases') == False:
        os.mkdir('databases')
    file = open('database/users.json', 'w')
    file.write(json.dumps([]))
    file.close()
    return open('database/users.json', 'r')
def user_add():
    user = {
        "first_name": input("First Name: "),
        "last_name": input("Last Name: "),
        "Email": input("Email: "),
    }
    try:
        file = open('database/users.json', 'r')
    except FileNotFoundError:
           file = create_file()
    all_users_data_json = file.read()
    all_users_data = json.loads(all_users_data_json)
    file.close()
    if len(all_users_data) > 0:
        user['id'] = all_users_data[-1]['id'] + 1
    else:
        user['id'] = 1
    if check_email(user['Email'], all_users_data) == False:
        all_users_data.append(user)
        with open('database/users.json', 'w') as file:
            file.write(json.dumps(all_users_data))
    else:
        print("User with this email already exist!!!")

def get_all():
    with open('database/users.json', 'r') as file:
        users = json.loads(file.read())
        for user in users:
            print("User #" + str(user['id']))
            print("First Name: " + user['first_name'])
            print("Last Name: " + user['last_name'])
            print("Email: " + user['Email'])

#HW9 LOGGING & EXCEPTIONS
#When input value which is not in databese program returns error(FileNotFoundError)
def search_by(search_str, what_to_search):
  try:
    with open('database/users.json', 'r') as file:
        users = json.loads(file.read())
        for user in users:
            if str(user[what_to_search]).lower() == str(search_str).lower():
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['Email'])
  except FileNotFoundError:
      print('No such value in database')
      logging.warning("User input non-existent value")
def update_user():
    file = open('database/users.json', 'r')
    users = json.loads(file.read())
    file.close()
     #ValueError
    try:
        id = int(input("Type id of user which you want to update: "))
    except ValueError:
        print("Id must be number!")
        print("Enter number again")
        logging.warning(" Not integer id")
        id = int(input("Type id of user which you want to update: "))

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    for user in users:
        if user['id'] == id:
            user['first_name'] = first_name
            user['last_name'] = last_name
            user['Email'] = email

    with open('database/users.json', 'w') as file:
        file.write(json.dumps(users))
