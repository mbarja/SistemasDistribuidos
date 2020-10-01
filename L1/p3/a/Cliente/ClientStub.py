import grpc
import sys
import file_system_pb2_grpc, file_system_pb2
import time


class Stub:
    def __init__(self, host_port):
        self._appliance = host_port
        self._channel = None
        self._stub = None

    def connect(self):
        try:
            self._channel = grpc.insecure_channel(self._appliance)
            self._stub = file_system_pb2_grpc.FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, directorio):
        if self.is_connected():
            path = file_system_pb2.Path(value=directorio)
            response = self._stub.ListFiles(path)
            return response
        return None

    def open_file(self,archivo):
        if self.is_connected():
            path = file_system_pb2.Path(value=archivo)
            response = self._stub.OpenFile(path)
            return response
        return None

    def read_file(self,archivo):
        if self.is_connected():
            archivoLocal = open('.' + '//' + archivo, 'wb')
            offset=0
            cant_bytes=4000
            ts_inicio = int(round(time.time() * 1000))
            while True:

                RFParametros = file_system_pb2.ReadFileParameters(nombre_archivo=archivo, offset=offset, cant_bytes=cant_bytes)
                resp = self._stub.ReadFile(RFParametros)
                bytes_recibidos=sys.getsizeof(resp.contenido)
                archivoLocal.write(resp.contenido)
                if bytes_recibidos>(cant_bytes):
                    offset+=cant_bytes
                else:
                    print('transferencia finalizada')
                    archivoLocal.close()
                    break
            ts_final = int(round(time.time() * 1000))
            print('tiempo de transferencia: '+str(ts_final-ts_inicio))
            return True
        return None

    def close_file(self,archivo):
        if self.is_connected():
            path = file_system_pb2.Path(value=archivo)
            response = self._stub.CloseFile(path)
            return response
        return None