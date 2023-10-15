class Update:
    def __init__(self, db):
        self.db = db
        self.action = input('Was willst du aktualisieren? (1) Server, (2) Email, (3) Social Media: ')
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
        self.db.update_server(name, ip, username, password)
        print(f'Server aktualisiert! {name} - {ip} - {username} - [password]')


    def email(self):
        name = input('Name: ')
        email = input('Email: ')
        password = input('Password: ')
        self.db.update_email(name, email, password)
        print(f'Email aktualisiert! {name} - {email} - [password]')


    def social(self):
        name = input('Name: ')
        username = input('Username: ')
        email = input('Email: ')
        password = input('Password: ')
        self.db.update_social(name, username, email, password)
        print(f'Social Media aktualisiert! {name} - {username} - {email} - [password]')