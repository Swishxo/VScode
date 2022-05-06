import socket
import threading


#Returns the host ip adress dynamicaly 
SERVER = socket.gethostbyname(socket.gethostname())

#Choose a port to connect to you ip adress
PORT = 5050

#Your ip adress and port is placed in tuple 
#and stored as your Adress for clients to connect to
ADDRESS = (SERVER, PORT)

#Choose the format to send and recive messages
FORMAT = "utf-8"

# Lists that will contain
# the clients connected to the host
clients = []

#Lists that will contain
#the names connected to host
names = [] 

# Create a new socket for host, ---> socket.socket()
    #args1: Allows communication within a specific network environment
    #args2: This socket type transmits data on a reliable basis, in sequence
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the address to the socket
server.bind(ADDRESS)

#function start the connection
def startChat():

    #returns host ip adress
	print("server is working on " + SERVER)
	
	#listen(): listening for incoming connections
        #specified or unspecified
	server.listen()
	
    #run an endless loop to continuosly accept connections
	while True:
	
		#accept():returns sockets that are connected to the client
            #the two things returned are the "conn and addr"
            #"conn == client ip" and "addr == avaliable client port" 
		conn, addr = server.accept()

        #send message to client
		conn.send("NAME".encode(FORMAT))
		
		#1024 represents the max amount of data that can be received in bytes
		name = conn.recv(1024).decode(FORMAT)
		
		#every name is added to the list names
		names.append(name)

        #every new connection is added to the client list
		clients.append(conn)
		
		print(f"Name is :{name}")
		
		#broadcast message function
            #pass a formated string w/ {name}, encoded
		broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
		
        #send message to client, endcoded
		conn.send('Connection successful!'.encode(FORMAT))
		
		# Start the handling thread
            #create a thread
            #arg1: target the function==handle()
            #args2: is the parameters for the function
        #Purpose:of thread, while sending message to client we can accept message @ the sametime
		handle_thread = threading.Thread(target = handle, args = (conn, addr))

        #start the thread
		handle_thread.start()
		
		# number of nodes connected to the server
		    #Counts number of threads running minus main() 
		print(f"active connections {threading.activeCount()-1}")

#method purpose to handle the incoming messages
def handle(conn, addr):

    #display connection added to host/server
	print(f"new connection {addr}")

    #create a boolean for loop
	connected = True
	
	while connected:
		#receive message w/ specified byte length
		message = conn.recv(1024)
		
		#pass message variable
        #to function broadcast message
		broadcastMessage(message)
	
	#close the connection
    #once message is recived from clients
	conn.close()

# method for broadcasting
# messages to the each clients
def broadcastMessage(message):
	for client in clients:
		client.send(message)

# call the method to
# begin the communication
startChat()
