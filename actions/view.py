class View:
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
        self.db.view_server(name)


    def email(self):
        name = input('Name: ')
        self.db.view_email(name)


    def social(self):
        name = input('Name: ')
        self.db.view_social(name)