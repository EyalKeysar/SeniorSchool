__author__ = "Eyal Keysar"

import socket
from constants import *
from  tcp_by_size import send_with_size ,recv_by_size


class ServerAPI():
    def __init__(self) -> None:
        self.cli_s = socket.socket()

    def connect(self):
        self.cli_s.connect((SERVER_IP,SERVER_PORT))

    def get_socket(self):
        return self.cli_s
    
    def send(self,data):
        send_with_size(self.cli_s,data)

    def recv(self):
        return recv_by_size(self.cli_s)
