import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 4000))
max_size = 8000

lin = sock.recv(max_size)
fitch = open(lin, 'w')

while(True):
    lin = sock.recv(max_size)
    fitch.write(lin.decode("utf-8"))
