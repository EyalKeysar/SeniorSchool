import socket

from ..shared.NetConst import *
from db_handler import DBHandler

import threading

HOST = '0.0.0.0'

class Server:
    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        
        self.db = DBHandler()
        
        self.clients = []
        self.usernames = []
        
        self.protocol_dict = {
            LOGIN_REQ: self.login,
            REGISTER_REQ: self.register
        }
        
    def run(self):
        while True:
            conn, addr = self.sock.accept()
            self.clients.append(conn)
            print(f"Client connected from {addr}")
            
            thread = threading.Thread(target=self.handle_client, args=(conn,))
            thread.start()
            
    def handle_client(self, conn):
        while True:
            data = conn.recv(1024).data.decode()
            if not data:
                break
            
            command = data[:6]
            
            if(self.dict[data[:6]] == None):
                print("Invalid command: " + data[:6])
            else:
                self.protocol_dict[command](data)
        
    def login(self, data):
        username, password = data[6:].split(";")
        
        if(self.db.login(username, password)):
            self.clients[self.usernames.index(username)].send(LOGIN_SUCCESS)
        else:
            self.clients[self.usernames.index(username)].send(LOGIN_FAIL)
        
        
    
    def register(self, data):
        username, password = data[6:].split(";")
        
        if(self.db.register(username, password)):
            self.clients[self.usernames.index(username)].send(REGISTER_SUCCESS)
        else:
            self.clients[self.usernames.index(username)].send(REGISTER_FAIL)