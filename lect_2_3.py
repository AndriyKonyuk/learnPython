import os


class AOpen:
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

        mode_list = [('r', os.O_RDONLY), ('w', os.O_WRONLY | os.O_CREAT), ('x', os.O_WRONLY | os.O_EXCL),
                     ('a', os.O_APPEND | os.O_CREAT), ('+', os.O_RDWR | os.O_CREAT)]  # mode 't' and 'b' not exist in module os
        mode_dict = {key: value for key, value in mode_list}
        if self.mode in mode_dict:
            self.mode = mode_dict[self.mode]
        self.open_file = os.open(self.filename, self.mode)

    def read(self):
        os.lseek(self.open_file, 0, os.SEEK_SET)
        return os.read(self.open_file, os.stat(self.open_file).st_size).decode('utf-8')

    def readLine(self):
        pass

    def write(self, s:str):
        if self.mode == os.O_WRONLY | os.O_CREAT:
            os.ftruncate(self.open_file, 0)
            os.lseek(self.open_file, 0, os.SEEK_SET)
            os.write(self.open_file, s.encode())

        else:
            os.lseek(self.open_file, os.stat(self.open_file).st_size, os.SEEK_SET)
            os.write(self.open_file, s.encode())

    def writeLine(self, s):
        pass

    def close(self):
        os.close(self.open_file)


filepath = 'file.txt'
x = AOpen(filepath, 'r')
x.write("hello world \n this is test")
print(x.read())
