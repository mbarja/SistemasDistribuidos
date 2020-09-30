import socket

def main():
    server_address = (('192.168.0.106', 8080))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_address)
    clienteActivo = True
    comandoFinalizarCliente = 'ExitCliente'

    while clienteActivo:
        print('Cliente activo')
        print('************************************************************')
        print("ingrese un mensaje a enviar al servidor: ")
        comando = input()
        if comando=='q':
            client.close()
            break
        client.send(comando.encode('utf-8'))

        data = client.recv(4096)
        from_server=data.decode()
        if (from_server == comandoFinalizarCliente):
            print('Servidor finalizado. Finalizar cliente')
            clienteActivo=False
        else:
            print(from_server)

    client.close()
    print('cliente desconectado')

if __name__ == '__main__':
    main()

