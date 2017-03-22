import os


class AOpen:
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

        mode_list = [('r', os.O_RDONLY), ('w', os.O_WRONLY | os.O_CREAT), ('x', os.O_WRONLY | os.O_EXCL),
                     ('a', os.O_APPEND), ('+', os.O_RDWR)]  # mode 't' and 'b' not exist in module os
        mode_dict = {key: value for key, value in mode_list}
        if self.mode in mode_dict:
            self.mode = mode_dict[self.mode]
        self.open_file = os.open(self.filename, self.mode)

    def read(self):
        return os.read(self.open_file, os.stat(self.open_file).st_size).decode('UTF-8')
        # (os.read(y, os.stat(y).st_size)).decode('UTF-8')

    def readLine(self):
        pass

    def write(self, s):
        pass

    def writeLine(self, s):
        pass

    def close(self):
        pass


filepath = 'file.txt'
x = AOpen(filepath)
print(x.read())
