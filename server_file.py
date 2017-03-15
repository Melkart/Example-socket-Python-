import socket
MAX_CLIENTS = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 4000)) #puerto 4000
sock.listen(MAX_CLIENTS)
coding = "utf-8"

#with sirve para declarar un bloque de codigo,
#fuera de su ambito se destruyen las variables
#leer de fichero:
#with open("test.py") as file:
#	for line in file:
#		print(line, end="")

while(True):
	(client,address) = sock.accept()
	client.sendall(bytes("server_file.py",encoding=coding))
	file = open("server_file.py")
	for line in file:
		client.sendall(bytes(line, encoding=coding))
	file.close()
