''' Week 3 assignment - encodes a given webpage into Unicode, sends GET request 
for header and content, receives relevant data and displays all
parameters such as Content Type, Content Length from the headers, etc. '''

import socket


def soc():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()


def main():
    soc()


if __name__ == "__main__":
    main()
