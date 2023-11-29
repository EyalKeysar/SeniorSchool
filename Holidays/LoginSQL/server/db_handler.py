import hashlib
import sqlite3
import random

DB_PATH = './authdb.db'
PEPPER = "50m3 p3pp3r"

class DBHandler:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.open_db()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, passwordSHA256 TEXT, salt TEXT)")
        self.commit_db()
        self.close_db()
        
    def open_db(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

    def commit_db(self):
        self.conn.commit()

    def close_db(self):
        self.conn.close()

    def login(self, username, password):

        self.open_db()
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cur.fetchone()

        #salted
        res = False
        if(user == None):
            res = False
        elif(user[1] == hashlib.sha256((password + user[2] + PEPPER).encode()).hexdigest()):
            res = True
        # elif(user[1] == hashlib.sha256(password.encode()).hexdigest()):
        #     res = True
    
        self.close_db()
        return res
        
    def register(self, username, password):
        self.open_db()
        self.cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cur.fetchone()
        
        if(user != None):
            self.close_db()
            return False
        
        #salted
        salt = str(random.randint(0, 1000000000))
        self.cur.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashlib.sha256((password + salt + PEPPER).encode()).hexdigest(), salt))
        # self.cur.execute("INSERT INTO users VALUES (?, ?)", (username, hashlib.sha256(password.encode()).hexdigest()))
        self.commit_db()
        self.close_db()
        return True

    def printall(self):
        self.open_db()
        self.cur.execute("SELECT * FROM users")
        print(self.cur.fetchall())
        self.close_db()