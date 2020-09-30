import socket
import random
from structures import payload_X

server_address = (('192.168.0.106', 8081))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

keep_working = True
client_id = random.randint(100000, 999999)

COMMAND = {'A': 1, 'O': 2}

acumulador=0

while keep_working:
	print('\n---------------------------------------------------')
	print('Ingrese un comando ([A]cumular, [O]btener, [S]alir)')
	comando = input()

	if comando == 'A':
		print('Ingrese un valor a acumular')
		valor = int(input())
		payload = payload_X(acumulador, COMMAND[comando], valor)
		client.sendall(payload)
		data = client.recv_into(payload)
		acumulador = payload.token
		print(f'El valor acumulado es: {acumulador}')

	elif comando == 'O':
		print(f'El valor acumulado es: {acumulador}')

	elif comando == 'S':
		keep_working = False
		client.close()
		print('Sesion finalizada')	

	else:
		print('El comando ingresado no es valido')
