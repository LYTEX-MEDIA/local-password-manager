
class Add:
    def __init__(self, db):
        self.db = db
        self.action = input('Was willst du hinzufügen? (1) Server, (2) Email, (3) Social Media: ')
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
        ip = input('IP Adresse: ')
        username = input('Username: ')
        password = input('Password: ')
        self.db.add_server(name, ip, username, password)
        print(f'Server hinzugefügt! {name} - {ip} - {username} - [password]')


    def email(self):
        name = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')
        self.db.add_email(name, email, password)
        print(f'Email hinzugefügt! {name} - {email} - [password]')


    def social(self):
        name = input('Name: ')
        username = input('Username: ')
        password = input('Password: ')
        self.db.add_social(name, username, password)
        print(f'Social Media Konto hinzugefügt! {name} - {username} - [password]')