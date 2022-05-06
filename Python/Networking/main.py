#Basic Python TCP Socket Server

#first import socket module
import socket 

#setup TCP connection for soc-server 
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect ip adress and port-number to soc-server
soc.bind(('127.0.0.1', 65028))

#soc-server waits for client to connect
soc.listen()

while True:
    #accept incoming message from client
    client, adress = soc.accept()
    print("connect to {}".format(adress))
    client.send("You are connected!".encode())
    client.close()