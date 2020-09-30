import os

class FS:
    def __init__(self):
        self._file_manager = {}
        self._path=''
        print('se crea file manager')

    def listar_archivos_(self,path):
        try:
            self._path=path
            return os.listdir(path)
        except Exception as e:
            print('ERROR!!! ', e)
            return None

    def open_file(self,path):
        try:
            if path not in self._file_manager:
                print(path)
                _path = os.path.join(self._path, path)
                _file = open(_path, 'rb')
                self._file_manager[path] = _file
                print(self._file_manager)
            return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False

    def read_file(self,path,offset,cant_bytes):
        try:
            if path not in self._file_manager:
                _path = os.path.join(self._path, path)
                _file = open(_path,'rb')
                self._file_manager[path] = _file
            else:
                _file=self._file_manager[path]
            _file.seek(offset)
            bytes_leidos = _file.read(cant_bytes)
            return bytes_leidos
        except Exception as e:
            print('ERROR en Read File!!! ', e)
            return None

    def close_file(self,path):
        try:
            if path in self._file_manager:
                self._file_manager[path].close()
                del self._file_manager[path]
                return True
        except Exception as e:
            print('ERROR!!! ', e)
            return False