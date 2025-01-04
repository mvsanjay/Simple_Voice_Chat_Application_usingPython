import socket
import cv2
import pickle
import struct
import imutils
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Server socket
# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 10050
socket_address = (host_ip,port)
print('Socket created')
# bind the socket to the host. 
#The values passed to bind() depend on the address family of the socket
server_socket.bind(socket_address)
print('Socket bind complete')
#listen() enables a server to accept() connections
#listen() has a backlog parameter. 
#It specifies the number of unaccepted connections that the system will allow before refusing new connections.
server_socket.listen(5)
print('Socket now listening')
connection, address=server_socket.accept()

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

while True:
    data = connection.recv(CHUNK)
    stream.write(data)

connection.close()
server_socket.close()

