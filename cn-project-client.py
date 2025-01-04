import socket
import cv2
import pickle
import struct
import imutils
import pyaudio
# Client socket
# create an INET, STREAMing socket : 
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '10.14.143.86' # Standard loopback interface address (localhost)
port = 10050 # Port to listen on (non-privileged ports are > 1023)
# now connect to the web server on the specified port number
client_socket.connect((host_ip,port)) 

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

while True:
    data = stream.read(CHUNK)
    client_socket.sendall(data)

client_socket.close()

