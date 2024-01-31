from shared.NetConst import *
import socket
from shared.core_proto import *

class ServerAPI():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        
        
    def login(self, username, password):
        send_by_size(self.sock, (LOGIN_REQ + username + ";" + password))
        response = self.sock.recv(1024).decode()
        
        if(response == LOGIN_SUCCESS):
            return True
        else:
            return False
        
    def register(self, username, password):
        send_by_size(self.sock, (REGISTER_REQ + username + ";" + password))
        response = self.sock.recv(1024).decode()
        
        if(response == REGISTER_SUCCESS):
            return True
        else:
            return False
        
        
        