from data.database import Database

class PasswordManager:
    def __init__(self):
        self.db = Database('db.sqlite3')