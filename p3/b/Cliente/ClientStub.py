import socket
import sys
import pickle
import time

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        mensaje = {
            "op": "1",
            "path": path
        }
        data_string = pickle.dumps(mensaje)
        self._channel.send(data_string)
        list_files = []
        try:
            data = self._channel.recv(1000000)
            data_loaded = pickle.loads(data)
            if not data:
                return list_files
            return data_loaded
        except Exception as e:
            print('ERROR en listFiles ', e)
            return

    def OpenFile(self,path):
        mensaje = {
            "op": "2",
            "path": path
        }
        data_string = pickle.dumps(mensaje)
        self._channel.send(data_string)
        try:
            data = self._channel.recv(1000000)
            data_loaded = pickle.loads(data)
            if not data:
                return None
            return data_loaded
        except Exception as e:
            print('ERROR en OpenFile ', e)
            return

    def ReadFile(self,path):
        offset=0
        cant_bytes=4000
        try:
            ts_inicio = int(round(time.time() * 1000))
            archivoLocal = open('.'+'//' + path, 'wb')
            while True:
                mensaje = {
                    "op": "3",
                    "path": path,
                    "offset": offset,
                    "cant_bytes":cant_bytes
                }
                data_string = pickle.dumps(mensaje)
                self._channel.send(data_string)
                bytes_recibidos = self._channel.recv(cant_bytes)
                cant_bytes_recibidos = sys.getsizeof(bytes_recibidos)
                archivoLocal.write(bytes_recibidos)
                if cant_bytes_recibidos > cant_bytes:
                    offset += cant_bytes
                else:
                    archivoLocal.close()
                    print('transferencia finalizada')
                    break
            ts_final = int(round(time.time() * 1000))
            print('tiempo de transferencia: ' + str(ts_final - ts_inicio))
            return True
        except Exception as e:
            print('ERROR en REadfile ', e)
            return False

    def CloseFile(self,path):
        mensaje = {
            "op": "4",
            "path": path
        }
        data_string = pickle.dumps(mensaje)
        self._channel.send(data_string)
        try:
            data = self._channel.recv(1000000)
            data_loaded = pickle.loads(data)
            if not data:
                return None
            return data_loaded
        except Exception as e:
            print('ERROR en CloseFile ', e)
            return

    def Desconectar(self):
        mensaje = {
            "op": "5",
            "path": ""
        }
        data_string = pickle.dumps(mensaje)
        try:
            self._channel.send(data_string)
        except Exception as e:
            print('ERROR en OpenFile ', e)
            return


class Stub:

    def __init__(self, host, port):
        self._appliance = (host, port)
        self._channel = None
        self._stub = None

    def connect(self):
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        if self.is_connected():
            self._stub.Desconectar()
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, path):
        if self.is_connected():
            return self._stub.ListFiles(path.strip())
        return 'El servidor esta desconectado'

    def open_file(self,path):
        if self.is_connected():
            return self._stub.OpenFile(path.strip())
        return 'El servidor esta desconectado'

    def read_file(self,path):
        if self.is_connected():
            return self._stub.ReadFile(path.strip())
        return 'El servidor esta desconectado'

    def close_file(self,path):
        if self.is_connected():
            return self._stub.CloseFile(path.strip())
        return 'El servidor esta desconectado'