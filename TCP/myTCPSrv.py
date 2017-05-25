from socket import *
from mensagem import Mensagem
import json
import time

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
timeout_val = 3.0
conn = ""
client_address = ""
server_socket.settimeout(timeout_val)
seq_num = 0


def my_accept():
    message = ""
    server_socket.settimeout(None)
    while (message != "SYN"):
        message, client_address = server_socket.recvfrom(2048)
    server_socket.settimeout(timeout_val)
    while (message != "ACK"):
        server_socket.sendto("SYNACK", client_address)
        try:
            message, client_address = server_socket.recvfrom(2048)
        except timeout:
            print "Connection timed out, retrying"

        print "Recieved", message
    return client_address


if __name__ == '__main__':
    print 'The server is ready to receive'
    while 1:
        # estabelece conexao com um cliente
        if conn == "":
            conn = my_accept()
            print "Estabilished connection with", conn

        # recebe mensagens exclusivamente desse cliente
        server_socket.settimeout(None)
        client_address = ""
        while (client_address != conn):
            message_serial, client_address = server_socket.recvfrom(2048)
            if client_address != conn:
                print "Ignored:", message_serial, "from:", client_address

        # finaliza a conexao com um cliente
        if message_serial == "END":
            conn = ""
            seq_num = 0
            print "Connection finished"
            continue

        # transforma a mensagem do cliente para uppercase e envia de volta
        print message_serial
        message = json.loads(message_serial)
        print "From client:", client_address, "Mensagem:", message['data']
        server_socket.settimeout(timeout_val)
        time.sleep(0.5)
        modified_mensagem = Mensagem(
            seq_num, message['data'].upper())
        print seq_num
        seq_num = seq_num + 1
        modified_mensagem_serial = json.dumps(modified_mensagem.__dict__)
        server_socket.sendto(modified_mensagem_serial, client_address)
