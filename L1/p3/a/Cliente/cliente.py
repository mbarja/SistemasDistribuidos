from Client import Client
from p3.a.Cliente.ClientStub import Stub

def main():
	stub = Stub('localhost:50051')
	cliente = Client(stub)
	cliente.conectar()
	keep_working = True
	while keep_working:
		print('************************************************************')
		print('Ingrese un comando ([L]ist, [O]pen, [R]ead, [C]lose, [S]alir')
		comando = input()
		if comando == 'L':
			print('Ingrese un directorio')
			directorio=input()
			archivos = cliente.listar_archivos(directorio)
			print (archivos.values)
		if comando=='O':
			print('Ingrese un archivo del directorio')
			nombreArchivo = str(input())
			respuesta = cliente.abrir_archivo(nombreArchivo.strip())
			print(respuesta.respuesta)
		if comando=='R':
			print('Ingrese un archivo del directorio')
			nombreArchivo = str(input())
			respuesta = cliente.leer_archivo(nombreArchivo.strip())
			if respuesta:
				print('Archivo copiado')
			else:
				print('Error al abrir archivo')
		if comando=='C':
			print('Ingrese un archivo del directorio')
			nombreArchivo = str(input())
			respuesta = cliente.cerrar_archivo(nombreArchivo.strip())
			print(respuesta.respuesta)
		if comando=='S':
			print('Salir')
			cliente.desconectar()
			keep_working = False


if __name__ == '__main__':
	main()