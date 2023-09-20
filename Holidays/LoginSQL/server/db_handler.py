import hashlib
import sqlite3

DB_PATH = './authdb.db'

class DBHandler:
    def __init__(self):
        
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, passwordSHA256 TEXT)")
        self.conn.commit()
        
    def login(self, username, password):
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cur.fetchone()
        
        if(user == None):
            return False
        
        if(user[1] == hashlib.sha256(password.encode()).hexdigest()):
            return True
        else:
            return False
        
    def register(self, username, password):
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cur.fetchone()
        
        if(user != None):
            return False
        
        self.cur.execute("INSERT INTO users VALUES (?, ?)", (username, hashlib.sha256(password.encode()).hexdigest()))
        self.conn.commit()
        
        return True