from cryptography.fernet import Fernet
import sqlite3
import json

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.load_config()
        self.key = self.load_key()
        self.cipher_suite = Fernet(self.key)


    def load_key(self):
        with open('secret.key', 'rb') as f:
            return f.read()

    def load_config(self):
        with open('categories.json', 'r') as f:
            self.config = json.load(f)


    def create_table(self, category_name, fields):
        fields_line = ', '.join([f"{name} {datatype}" for name, datatype in fields.items()])
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {category_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, {fields_line})''')
        self.conn.commit()


    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode()).decode()


    def decrypt(self, data):
        return self.cipher_suite.decrypt(data.encode()).decode()


    def add_entry(self, category, **kwargs):
        fields = ', '.join(kwargs.keys())
        values = tuple(self.encrypt(value) if key == 'password' else value for key, value in kwargs.items())
        placeholders = ', '.join('?' for _ in kwargs)
        self.cursor.execute(f'''INSERT INTO {category}({fields}) VALUES({placeholders})''', values)
        self.conn.commit()


    def view_entry(self, category, identifier):
        self.cursor.execute(f'''SELECT * FROM {category} WHERE name=?''', (identifier,))
        result = self.cursor.fetchone()
        if result:
            fields = self.config[category]['fields'].keys()
            values = [self.decrypt(value) if field == 'password' else value for field, value in zip(fields, result[1:])]
            print("\n" + "\n".join(f"{field}: {value}" for field, value in zip(fields, values)) + "\n")
        else:
            print('Eintrag nicht gefunden.')


    def delete_entry(self, category, identifier):
        self.cursor.execute(f'''DELETE FROM {category} WHERE name=?''', (identifier,))
        self.conn.commit()


    def update_entry(self, category, identifier, **kwargs):
        fields = ', '.join(f"{key}=?" for key in kwargs)
        values = tuple(self.encrypt(value) if key == 'password' else value for key, value in kwargs.items()) + (identifier,)
        self.cursor.execute(f'''UPDATE {category} SET {fields} WHERE name=?''', values)
        self.conn.commit()


    def close(self):
        self.conn.close()