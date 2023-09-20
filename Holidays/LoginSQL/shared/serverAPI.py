from .NetConst import *
import socket

class ServerAPI():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        
    def login(self, username, password):
        self.sock.send(LOGIN_REQ + username + ";" + password)
        response = self.sock.recv(1024).decode()
        
        if(response == LOGIN_SUCCESS):
            return True
        else:
            return False
        
    def register(self, username, password):
        self.sock.send(REGISTER_REQ + username + ";" + password)
        response = self.sock.recv(1024).decode()
        
        if(response == REGISTER_SUCCESS):
            return True
        else:
            return False
        
        
        