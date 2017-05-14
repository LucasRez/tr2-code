from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# Define o maximo de conexoes que o servidor escuta de uma vez
maxlisten = 2
# Lista de requisicoes de conexao
backlog = []
# Lista de conexoes sendo escutadas
listening = []
# mensagens das conexoes sendo escutadas
listenmsgs = {}
# Numero de conexoes sendo escutadas
listen = 0

clientDest = None
# garantir a ordem das mensagens
print 'The server is ready to receive'
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    # recebe as requisicoes de conexao
    if (message == "SYN"):
        backlog.insert(0, clientAddress)
        print "Connect to: ", backlog[-1:]
        # aceita as conexoes se estiver de acordo com o limite de conexoes definido
        if (listen < maxlisten):
            clientDest = backlog.pop()
            print "Client to listen:", clientDest
            listening.insert(0, clientDest)
            print listening[-1:]
            listen = listen + 1
            serverSocket.sendto("ACK", clientDest)
            clientDest = None
    # recebe as demais mensagens
    else:
        listenmsgs[clientAddress] = message
        print "Message:", message, "From:", clientAddress
        # responde as conexoes sendo escutadas na ordem
        if (len(listening) > 0):
            clientDest = listening.pop()
            print "Client to send:", clientDest
            listen = listen - 1
            print listenmsgs
            sentence = listenmsgs[clientDest]
            del(listenmsgs[clientDest])
            print "From Client: ", sentence
            reply = sentence.upper()
            serverSocket.sendto(reply, clientDest)
