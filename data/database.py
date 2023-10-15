import sqlite3

class Database:
    def __init__(self, db_name):    
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    
    def get_table(self, table_name):
        self.cursor.execute('''SELECT * FROM {}'''.format(table_name))
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()