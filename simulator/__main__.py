from models.database.master import Master
from models.database.slave import Slave

mater = Master()
slave = Slave()

while True:
    print('Enter "1" to create user')
    print('Enter "2" to get users')
    print('Enter "3" to get user')
    print('Enter "4" to delete user')
    print('Enter "5" to update user')
    print('Enter "6" to exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        name = input('Enter name: ')
        username = input('Enter username: ')
        password = input('Enter password: ')
        mater.create_user(name, username, password)
    elif choice == '2':
        users = mater.get_users()
        for user in users:
            print(user)
    elif choice == '3':
        user_id = input('Enter user id: ')
        user = mater.get_user(user_id)
        print(user)
    elif choice == '4':
        user_id = input('Enter user id: ')
        mater.delete_user(user_id)
    elif choice == '5':
        user_id = input('Enter user id: ')
        name = input('Enter name: ')
        username = input('Enter username: ')
        password = input('Enter password: ')
        mater.update_user(user_id, name, username, password)
    elif choice == '6':
        break
