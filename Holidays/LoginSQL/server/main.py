import socket
import threading
from hashlib import sha256, md5

from shared.NetConst import *
from shared.core_proto import *
from server.db_handler import DBHandler


HOST = '0.0.0.0'
HASH_PEPPER = "50m3 p3pp3r"

class Server:
    def __init__(self):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        
        self.db = DBHandler()
        
        self.clients = []
        self.authenticated_clients = []
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
            data = recv_by_size(conn)
            if not data:
                break
            
            command = data[:6]
            
            if(self.protocol_dict[data[:6]] == None):
                print("Invalid command: " + data[:6])
            else:
                self.protocol_dict[command](conn, data)
            self.db.printall()

    def login(self, conn, data):
        username, password = data[6:].split(";")
        
        if(self.db.login(username, password)):
            conn.send(LOGIN_SUCCESS.encode())
            if(conn not in self.authenticated_clients):
                self.authenticated_clients.append(conn)
        else:
            conn.send(LOGIN_FAIL.encode())
        
    
    def register(self, conn, data):
        username, password = data[6:].split(";")
        
        if(self.db.register(username, password)):
            conn.send(REGISTER_SUCCESS.encode())
            if(conn not in self.authenticated_clients):
                self.authenticated_clients.append(conn)
        else:
            conn.send(REGISTER_FAIL.encode())
if(__name__ == "__main__"):
    server = Server()
    server.run()