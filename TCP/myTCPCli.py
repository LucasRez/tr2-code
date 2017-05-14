from socket import *
serverName = ''
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto("SYN",(serverName, serverPort))
response, serverAddress = clientSocket.recvfrom(2048)
if (response != "ACK"):
    print "Failed to establish connection, exiting..."
    clientSocket.close()
    exit()
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
