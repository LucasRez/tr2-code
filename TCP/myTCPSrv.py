from socket import *
from srvThread import *
import time

def myAccept():
    message = ""
    serverSocket.settimeout(None)
    while (message != "SYN"):
        message, clientAddress = serverSocket.recvfrom(2048)
    serverSocket.settimeout(timeoutVal)
    while (message != "ACK"):
        serverSocket.sendto("SYNACK", clientAddress)
        try:
            message, clientAddress = serverSocket.recvfrom(2048)
        except timeout:
            print "Connection timed out, retrying"
            
        print "Recieved", message
    return clientAddress

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
timeoutVal = 3.0
serverSocket.settimeout(timeoutVal)
print 'The server is ready to receive'
conn = ""
clientAddress = ""
while 1:
    conn = myAccept()
    print "Estabilished connection with", conn
    serverSocket.settimeout(None)
    while (clientAddress != conn):
        message, clientAddress = serverSocket.recvfrom(2048)
        if clientAddress != conn:
            print "Got", message, "from: ", clientAddress
    print "From client:", clientAddress, "Message:", message
    serverSocket.settimeout(timeoutVal)
    time.sleep(0.5)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)

