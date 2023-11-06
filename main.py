from data.database import Database
from actions.view import View
from actions.add import Add
from actions.delete import Delete
from actions.update import Update
from data.categories import Categories

class PasswordManager:
    def __init__(self):
        self.db = Database('db.sqlite3')
        self.categories = Categories()
        self.create_tables()
        self.display_welcome_message()
        self.select_action()
       
 
    def display_welcome_message(self):
        print("""
              LYTEX MEDIA | Password Manager
              
              yoo dieses Skriptchen ist nicht sonderlich sicher.
              Die Passwörter werden fast im Klartext in der Datenbank gespeichert. xD
              Aber trotzdem nützlich für mich. Pass einfach auf,
              dass niemand Zugriff auf die Dateien bekommt!
              """)


    def select_action(self):
        action = input('Was willst du tun? (1) View, (2) Add, (3) Delete, (4) Update, (5) Exit: ')
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
            print('Ungültige Eingabe!')
            self.select_action()


    def create_tables(self):
        for category_name, category_info in self.categories.get_all_categories().items():
            self.db.create_table(category_name, category_info['fields'])


if __name__ == '__main__':
    manager = PasswordManager()
    while True:
        manager.select_action()