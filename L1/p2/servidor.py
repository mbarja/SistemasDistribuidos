import socket

from structures import *

server_address = (('192.168.0.106', 8081))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

payload=payload_X()

while True:
	print('Server disponible!')
	connection, client_address = server.accept()	

	while True:
		print('-----------------')
		data = connection.recv_into(payload)
		if not data: break
		
		if payload.operation == 1:
			payload.token += payload.data
			connection.sendall(payload)

		elif payload.operation == 2:
			connection.sendall(payload)
			
		else:
			print(f'El cliente {payload.token} solicito el comando {payload.operacion} con el valor {payload.data}')
			break
		

	connection.close()
	print('cliente desconectado \n')
