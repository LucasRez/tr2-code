from socket import *
from mensagem import Mensagem
import json
import threading
import time

server_name = ''
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
timeout_val = 3.0
seq_num = 0
expected_seq = 0
base = 0
win_size = 4
resposta = ""
exit_event = threading.Event()


class Sender(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text

    def run(self):
        global seq_num, expected_seq, win_size, base, exit_event
        if win_size > len(self.text):
            win_size = len(self.text)
        while base < len(self.text):
            if exit_event.is_set():
                break
            if base + win_size > len(self.text):
                win_size = len(self.text) - base

            if base <= expected_seq + win_size - 1:
                while base <= expected_seq + win_size - 1:
                    print "seq_num:", seq_num
                    message = Mensagem(seq_num, text[seq_num])
                    print "sent", message.data
                    message_serial = json.dumps(message.__dict__)
                    client_socket.sendto(
                        message_serial, (server_name, server_port))
                    base = base + 1
                    seq_num = seq_num + 1

        client_socket.sendto("END", (server_name, server_port))


class Reciever(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.text = text

    def run(self):
        global expected_seq, resposta, exit_event
        while expected_seq < len(self.text):
            if exit_event.is_set():
                break
            try:
                modified_message_serial, server_address = client_socket.recvfrom(
                    2048)
            except timeout:
                print "\n[ERROR]Server can't be reached ending connection"
                exit_event.set()
                break
            modified_message = json.loads(modified_message_serial)
            print "recieved from server:", modified_message['data']
            resposta = resposta + modified_message['data']
            expected_seq = expected_seq + 1


def my_connect(addr):
    ack = ""
    print "Attempting to connect to server..."
    while ack != "SYNACK":
        client_socket.sendto("SYN", addr)
        try:
            ack, addr = client_socket.recvfrom(2048)
        except timeout:
            print "Connection timed out, retrying"
    client_socket.sendto("ACK", addr)
    print "Connection to server estabilished"


if __name__ == '__main__':
    client_socket.settimeout(timeout_val)
    my_connect((server_name, server_port))
    client_socket.settimeout(25)

    text = raw_input('Input lowercase sentence:')

    try:
        sender = Sender(text)
        reciever = Reciever(text)

        sender.start()
        reciever.start()

        while sender.is_alive() or reciever.is_alive():
            time.sleep(0.5)
    except KeyboardInterrupt:
        exit_event.set()

    sender.join()
    reciever.join()

    print "sent:", text
    print "recieved:", resposta

    client_socket.close()
