import concurrent
import socket
import sys
import pickle
import threading
from concurrent.futures.thread import ThreadPoolExecutor


class FSStub(threading.Thread):
    def __init__(self, canal, file_system_adapter):
        threading.Thread.__init__(self)
        self._channel = canal
        self._adapter = file_system_adapter
        self.run()





class Stub:
    def __init__(self, adapter, port):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._executor = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('192.168.0.106', self._port))
        self._executor = ThreadPoolExecutor(max_workers=2)

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                connection, client_address = self.server.accept()
                self._executor.submit(self.process_request, connection)
        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)

    def process_request(self, channel):
        try:
            while True:
                print(threading.get_ident())
                data = channel.recv(1000000)
                data_loaded = pickle.loads(data)
                comando = data_loaded["op"]
                path = data_loaded["path"]
                if comando == '1':
                    self.list_file(path,channel)
                if comando == '2':
                    self.open_file(path,channel)
                if comando == '3':
                    self.read_file(path, channel, data_loaded["offset"], data_loaded["cant_bytes"])
                if comando == '4':
                    self.close_file(path,channel)
                if comando == '5':
                    print("cliente desconectado")
                    channel.close()
                    break
        except Exception as e:
            print('ERROR!!! ', e)
            return

    def close_file(self, path,channel):
        respuesta = self._adapter.open_file(path)
        if (respuesta):
            respuesta = 'archivo cerrado'
        else:
            respuesta = 'error al cerrar archivo'
        data_string = pickle.dumps(respuesta)
        channel.send(data_string)

    def read_file(self, path, channel, offset, cant_bytes):
        print(path, offset, cant_bytes)
        bytesLeidos = self._adapter.read_file(path, offset, cant_bytes)
        print('enviando bytes' + str(sys.getsizeof(bytesLeidos)))
        channel.sendall(bytesLeidos)

    def open_file(self, path, channel):
        respuesta = self._adapter.open_file(path)
        if (respuesta):
            respuesta = 'archivo abierto'
        else:
            respuesta = 'error al abrir archivo'
        data_string = pickle.dumps(respuesta)
        channel.send(data_string)

    def list_file(self, path, channel):
        path_files = self._adapter.listar_archivos_(path)
        data_string = pickle.dumps(path_files)
        channel.send(data_string)