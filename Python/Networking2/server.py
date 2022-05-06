
import socket #needed to create connection 
import threading #allows different execution @ same time 


HEADER = 64 #assocaited with msg_length var
FORMAT = 'utf-8' #decodes incoming message in this format
DISCONNECT_MSG = "!DISCONNECT"

#SERVER = "192.168.1.225" #using personal ip adress as server, another option

PORT = 5050 #need empty port to assign connection
SERVER =  socket.gethostbyname(socket.gethostname())#automatically gets the server ip adress
ADDR = (SERVER,PORT)#bind SERVER and PORT into a tuple

#create socket connection for other devices to conect
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create type of ip connection to accept
server.bind(ADDR) #bind ADDR to server

#set server to wait for new incoming connections
def handle_client(conn, addr):
    print(f"[New CONNECTION] {addr} connected")

    connected = True
    while connected:
        #gets length of incoming message from client
        #.recv() is blocking function, code will pause here and wait for a message. will come in bytes
        msg_length = conn.recv(HEADER).decode(FORMAT) #decodes bytes into string FORMAT
        if msg_length:
            msg_length = int(msg_length) #covert size of string into an int
            #decode the int
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{addr}]:  {msg}") #display msg

    conn.close()

def start():#this function listens for connections
    server.listen()
    print(f" CURRENT incomming ip: {SERVER} Listening!")
    while True:
        #con = send info back to incoming conection
        #addr = stores ip address and port of incoming conection
        conn, addr = server.accept()#accept function waits for a new connection, .accept() function is a blocking call

        #after new connection is made
            #create a thread so other connections dont wait
        thread = threading.Thread(target =handle_client, args=(conn,addr))
        thread.start()
        print(f"[Active connection threads] {threading.activeCount() - 1}") #counts number of threads created from connections, "- 1" because one thread is currently active

        
print("Server is starting.....")
start()


