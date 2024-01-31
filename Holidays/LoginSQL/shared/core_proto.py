import socket
from Crypto.Cipher import AES


LEN_ENTRY_SEP = ';'
def send_by_size(sock, data):
    message = str(len(data)) + LEN_ENTRY_SEP + data
    sock.send(message.encode())
    
def recv_by_size(sock):
    str_num = ""
    cur = '0'
    while cur != LEN_ENTRY_SEP:
        str_num += cur
        cur = sock.recv(1).decode()
    num = int(str_num)
    data = sock.recv(num).decode()
    return data


def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return nonce + ciphertext + tag