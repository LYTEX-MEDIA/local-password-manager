import sqlite3

class Database:
    def __init__(self, db_name):    
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()


    def create_email_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS emails(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, password TEXT)''')
        self.conn.commit()


    def create_social_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS socials(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, username TEXT, email TEXT, password TEXT)''')
        self.conn.commit()
    
    
    def create_server_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS servers(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, ip TEXT, username TEXT, password TEXT)''')
        self.conn.commit()
    
    
    def add_server(self, name, ip, username, password):
        self.cursor.execute('''INSERT INTO servers(name, ip, username, password) VALUES(?,?,?,?)''', (name, ip, username, password))
        self.conn.commit()
    
    
    def add_email(self, name, email, password):
        self.cursor.execute('''INSERT INTO emails(name, email, password) VALUES(?,?,?)''', (name, email, password))
        self.conn.commit()
    
    
    def add_social(self, name, username, email, password):
        self.cursor.execute('''INSERT INTO socials(name, username, email, password) VALUES(?,?,?,?)''', (name, username, email, password))
        self.conn.commit()

    
    def view_server(self, name):
        self.cursor.execute('''SELECT * FROM servers WHERE name=?''', (name,))
        result = self.cursor.fetchone()
        print(f'\n Name: {result[1]}\n IP: {result[2]}\n Username: {result[3]}\n Password: "{result[4]}"\n')
    
    
    def view_email(self, name):
        self.cursor.execute('''SELECT * FROM emails WHERE name=?''', (name,))
        result = self.cursor.fetchone()
        print(f'\n Name: {result[1]}\n Email: {result[2]}\n Password: "{result[3]}"\n')
    
    
    def view_social(self, name):
        self.cursor.execute('''SELECT * FROM socials WHERE name=?''', (name,))
        result = self.cursor.fetchone()
        print(f'\n Name: {result[1]}\n Username: {result[2]}\n Email: {result[3]}\n Password: "{result[4]}\n"')
    
    
    def delete_server(self, name):
        self.cursor.execute('''DELETE FROM servers WHERE name=?''', (name,))
        self.conn.commit()

    
    def delete_email(self, name):
        self.cursor.execute('''DELETE FROM emails WHERE name=?''', (name,))
        self.conn.commit()
    
    
    def delete_social(self, name):
        self.cursor.execute('''DELETE FROM socials WHERE name=?''', (name,))
        self.conn.commit()
    
    
    def close(self):
        self.conn.close()