import os
from cryptography.fernet import Fernet
from data.database import Database
from actions.view import View
from actions.add import Add
from actions.delete import Delete
from actions.update import Update
from data.categories import Categories

class PasswordManager:
    def __init__(self):
        self.check_key()
        self.db = Database('db.sqlite3')
        self.categories = Categories()
        self.create_tables()
        self.display_welcome_message()
        self.select_action()
       
 
    def display_welcome_message(self):
        print("""
              -----------------------------------
              
               LYTEX MEDIA Password Manager
              
              -----------------------------------
              """)


    def select_action(self):
        action = input('What do you want to do? (1) View, (2) Add, (3) Delete, (4) Update, (5) Exit: ')
        action_map = {
            '1': View,
            '2': Add,
            '3': Delete,
            '4': Update,
            '5': exit
        }
        try:
            if action == '5':
                self.db.close()
                action_map[action]()
            else:
                action_map[action](self.db)
        except KeyError:
            print('Invalid action! Please try again')
            self.select_action()


    def create_tables(self):
        for category_name, category_info in self.categories.get_all_categories().items():
            self.db.create_table(category_name, category_info['fields'])


    def check_key(self):
        if not os.path.exists('secret.key'):
            print('Key not found! Creating a new key...')
            self.create_key()


    def create_key(self):
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as key_file:
            key_file.write(key)
            
        print('Key created successfully!')


if __name__ == '__main__':
    manager = PasswordManager()
    
    while True:
        manager.select_action()