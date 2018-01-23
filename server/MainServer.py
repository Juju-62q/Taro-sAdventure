import socket
from time import time

def main():
    host = "localhost" # 適宜変更すること
    port = 59630
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host,port))
    serversock.listen(10)

    while True:
        print('Waiting for connections from a client.')
        clientsock, client_address = serversock.accept()

        controlNum = int(clientsock.recv(4096).decode('ascii'))
        if controlNum == 1:
            print("now is 1")
            clientsock.sendall(b'connected')
            sendData = clientHighScore(59631)
            print(sendData)
            clientsock.sendall(sendData)

        elif controlNum == 2:
            print("now is 2")
            clientsock.sendall(b'connected')
            userName = clientsock.recv(4096)
            print(userName)
            sendData = clientUserScore(59632, userName)
            clientsock.sendall(sendData)

        elif controlNum == 3:
            print("now is 3")
            clientsock.sendall(b'connected')
            sendData = clientRanking(59633)
            clientsock.sendall(sendData)

        elif controlNum == 4:
            print("now is 4")
            clientsock.sendall(b'connected')
            userNameAndScore = clientsock.recv(4096)
            print(userNameAndScore)
            sendData = clientInsertScore(59634, userNameAndScore)
            clientsock.sendall(sendData)

    clientsock.close()

def clientHighScore(portNum):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", portNum))
    response = client.recv(4096)
    return response

def clientUserScore(portNum, userName):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", portNum))
    client.sendall(userName)
    response = client.recv(4096)
    print(response)
    return response

def clientRanking(portNum):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", portNum))
    response = client.recv(20000)
    print(response)
    return response

def clientInsertScore(portNum, userNameAndScore):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", portNum))
    now = str(int(time())).encode("ascii")
    print(userNameAndScore + now)
    client.sendall(userNameAndScore + now)
    response = client.recv(4096)
    print(response)
    return response

if __name__ == '__main__':
    main()
