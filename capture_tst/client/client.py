#!/usr/bin/python

from socket import *
HOST = 'localhost'
PORT = 20000
BUFSIZE = 1024
ADDR = (HOST ,PORT)



if __name__ == '__main__' :
	tcpClientSock = socket(AF_INET,SOCK_STREAM)


	tcpClientSock.connect(ADDR)

	while True:

		data=raw_input('Enter a string your want to send >')
		if not data:
			break
		tcpClientSock.send(data)
		data=tcpClientSock.recv(BUFSIZE)

		if not data:
			break
		print data


	tcpClientSock.close()
