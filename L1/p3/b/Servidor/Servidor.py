from L1.p3.b.Servidor.file_system import FS
from L1.p3.a.Servidor.Server import Server
from L1.p3.b.Servidor.ServerStub import Stub

def main():
    adaptador=FS()
    stub = Stub(adaptador, 50051)
    servidor = Server(stub)
    servidor.inicializar()

if __name__ == '__main__':
    main()