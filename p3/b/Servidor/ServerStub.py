import socket
import sys
import pickle

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        try:
            while True:
                data = self._channel.recv(1000000)
                data_loaded = pickle.loads(data)
                comando = data_loaded["op"]
                path = data_loaded["path"]
                if comando == '1':
                    self.list_file(path)
                if comando=='2':
                    self.open_file(path)
                if comando=='3':
                    self.read_file(path, data_loaded["offset"], data_loaded["cant_bytes"])
                if comando=='4':
                    self.close_file(path)
                if comando=='5':
                    print("cliente desconectado")
                    self._channel.close()
                    break
        except Exception as e:
            print('ERROR!!! ', e)
            return

    def close_file(self, path):
        respuesta = self._adapter.close_file(path)
        if (respuesta):
            respuesta = 'archivo cerrado'
        else:
            respuesta = 'error al cerrar archivo'
        data_string = pickle.dumps(respuesta)
        self._channel.send(data_string)

    def read_file(self, path, offset, cant_bytes):
        bytesLeidos = self._adapter.read_file(path, offset, cant_bytes)
        print('enviando bytes' + str(sys.getsizeof(bytesLeidos)))
        self._channel.sendall(bytesLeidos)


    def open_file(self, path):
        respuesta = self._adapter.open_file(path)
        if (respuesta):
            respuesta = 'archivo abierto'
        else:
            respuesta = 'error al abrir archivo'
        data_string = pickle.dumps(respuesta)
        self._channel.send(data_string)

    def list_file(self, path):
        path_files = self._adapter.listar_archivos_(path)
        data_string = pickle.dumps(path_files)
        self._channel.send(data_string)

class Stub:

    def __init__(self, adapter, port):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._stub = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('192.168.0.106', self._port))

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                print('server activo')
                connection, client_address = self.server.accept()
                self._stub = FSStub(connection, self._adapter)

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)