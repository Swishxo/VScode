#Basic Python TCP Socket Client
import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 65028))
msg = soc.recv(1024)
soc.close()

print(msg.decode())
