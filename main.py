from data.database import Database
from actions.view import View
from actions.add import Add
from actions.delete import Delete

class PasswordManager:
    def __init__(self):
        self.db = Database('db.sqlite3')
        self.create_tables()
        print("""
              LYTEX MEDIA | Password Manager
              
              yoo dieses Skriptchen ist nicht sonderlich sicher.
              Die Passwörter werden fast im Klartext in der Datenbank gespeichert. xD
              Aber trotzdem nützlich für mich. Pass einfach auf,
              dass niemand Zugriff auf die Dateien bekommt!
              """)
        self.select_action()


    def select_action(self):
        action = input('Was willst du tun? (1) View, (2) Add, (3) Delete, (4) Update, (5) Exit: ')
        if action == '1':
            View(self.db)
        elif action == '2':
            Add(self.db)
        elif action == '3':
            Delete(self.db)
            pass
        elif action == '4':
            # TODO: Update(self.db)
            pass
        elif action == '5':
            self.db.close()
            exit()
        else:
            print('Ungültige Eingabe!')
            self.select_action()


    def create_tables(self):
        self.db.create_email_tables()
        self.db.create_social_tables()
        self.db.create_server_tables()


if __name__ == '__main__':
    PasswordManager()