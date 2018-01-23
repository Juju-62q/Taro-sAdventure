import socket


def main():
    host = "localhost" # 適宜変更すること
    port = 59632
    unSendFlag = True
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind((host,port))
    serversock.listen(10)

    while True:
        print('Waiting for connections from a client.')
        clientsock, client_address = serversock.accept()

        userName = clientsock.recv(4096).decode('ascii').replace("\n","")
        for line in open('ranking.txt', 'r'):
            tmpList = line.split(" ")
            if tmpList[0] == userName:
                print(tmpList[1])
                clientsock.sendall(tmpList[1].encode('ascii'))
                unSendFlag = False
                break
        if unSendFlag:
            print("見つからんかった")
            clientsock.sendall(b'0')
            print("見つからんかったをおくりました")
    clientsock.close()



if __name__ == '__main__':
    main()
