import socket 
import thread
import time

sock=socket.socket()
host=socket.gethostname()
port=12345
sock.bind((host,port))
sock.listen