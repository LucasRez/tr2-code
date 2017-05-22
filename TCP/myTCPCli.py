from socket import *
def myConnect(addr):
	ack = ""
	while (ack != "SYNACK"):
		clientSocket.sendto("SYN", addr)
		try:
			ack, addr = clientSocket.recvfrom(2048)
		except timeout:
			print "Connection timed out, retrying"
	clientSocket.sendto("ACK", addr)

serverName = '' 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
timeoutVal = 3.0
clientSocket.settimeout(timeoutVal)

myConnect((serverName, serverPort))
clientSocket.settimeout(None)

message = raw_input('Input lowercase sentence:') 

clientSocket.sendto(message,(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print modifiedMessage
clientSocket.close()
