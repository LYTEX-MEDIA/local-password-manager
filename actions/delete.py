class Delete:
    def __init__(self, db):
        self.db = db
        self.action = input('In welche Kategorie möchtest du? (1) Server, (2) Email, (3) Social Media: ')
        if self.action == '1':
            self.server()
        elif self.action == '2':
            self.email()
        elif self.action == '3':
            self.social()
        else:
            print('Ungültige Eingabe!\n')
            self.__init__()


    def server(self):
        name = input('Name: ')
        self.db.delete_server(name)
        print(f'Server Account {name} gelöscht!\n')


    def email(self):
        name = input('Name: ')
        self.db.delete_email(name)
        print(f'Email Account {name} gelöscht!\n')


    def social(self):
        name = input('Name: ')
        self.db.delete_social(name)
        print(f'Social Media Account {name} gelöscht!\n')