import grpc
from concurrent import futures
import time
import sys

import file_system_pb2
from file_system_pb2_grpc import (
    add_FSServicer_to_server,
    FSServicer,
)


class StubFSServicer(FSServicer):

    def __init__(self, adapter):
        self._adapter = adapter
        FSServicer.__init__(self)

    def ListFiles(self, request, context):
        response = file_system_pb2.PathFiles()
        try:
            for file in self._adapter.listar_archivos_(request.value):
                response.values.append(file)
        except Exception as e:
            print('ERRR En server list files ', e)
        return response

    def OpenFile(self, request, context):
        response = file_system_pb2.ResultadoOpen()
        try:
            archivoAbierto = self._adapter.open_file(request.value)
            if (archivoAbierto):
                response.respuesta = 'Archivo abierto'
            else:
                response.respuesta = 'Error al abrir archivo'
        except Exception as e:
            print('ERRR En server open files ', str(e))
        return response

    def ReadFile(self, request, context):
        print(request.nombre_archivo,request.offset,request.cant_bytes)
        response = file_system_pb2.ResultadoRF()
        try:
            response.contenido = self._adapter.read_file(request.nombre_archivo, request.offset, request.cant_bytes)
            print(sys.getsizeof(response.contenido))
        except Exception as e:
            print('ERRR En server readFiles files ', str(e))
        return response

    def CloseFile(self, request, context):
        response = file_system_pb2.ResultadoClose()
        try:
            archivoCerrado = self._adapter.close_file(request.value)
            if(archivoCerrado) : response.respuesta = 'Archivo cerrado'
            else: response.respuesta = 'Error al cerrar archivo'
        except Exception as e:
            print('ERRR En server close files ', str(e))
        return response

class Stub:
    def __init__(self, adapter, port='50051'):
        self._port = port
        self._adapter = adapter
        self.server = None


    def _setup(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_FSServicer_to_server(StubFSServicer(self._adapter), self.server)
        self.server.add_insecure_port('[::]:{}'.format(self._port))


    def run(self):
        self._setup()
        self.server.start()
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)

