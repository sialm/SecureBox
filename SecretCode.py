from socket import socket, AF_INET, SOCK_STREAM, error
from struct import unpack, pack

BUF_SIZE = 4096
DECODE_CODE = '!I'
OPEN = 1
CLOSED = 0
SERVER_IP = '140.142.30.164' #'unimate.cs.washington.edu'
SERVER_PORT = 48102

def get_secret_code():
    secret_code = 0
    while secret_code is 0:
        print('getting code')
        secret_code = recv_secret_code()

    print('secret : ' + str(secret_code))
    secret_code = secret_code[0]
    return str(secret_code)

def recv_secret_code():
    """
    Waits to recieve the secret code (will block)
    :return:
    """
    try:
        print('trying to connect')
        srv_socket = socket(AF_INET, SOCK_STREAM)
        srv_socket.connect((SERVER_IP, SERVER_PORT))
        recv_data = srv_socket.recv(BUF_SIZE)
    except error:
        return 0

    secret_code = unpack(DECODE_CODE, recv_data)
    return secret_code

