import socket

def main():
	server_address = (('192.168.0.106', 8080))
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(server_address)
	server.settimeout(1000)
	server.listen()
	comandoExit='Exit'
	serverActivo = True
	connection, client_address = server.accept()
	print('Server disponible!')
	while serverActivo:
		from_client = ''
		data = connection.recv(10000000)
		if not data: break
		from_client += data.decode()
		print(from_client)
		if(from_client==comandoExit):
			message='ExitCliente'
			print('Finalizar servidor')
			serverActivo=False
		else:
			message='Mensaje recibido: '+ from_client
		connection.send(message.encode('utf-8'))

	connection.close()
	print('servidor desconectado \n')

if __name__ == '__main__':
    main()