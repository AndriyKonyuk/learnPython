from abc import ABC, abstractmethod
import csv, json

def csv_load(file: object) -> str:
    s = csv.reader(file, delimiter='\n')
    return s

def csv_save(s: str, file: object) -> None:
    spamwriter = csv.writer(file, delimiter=' ', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(s)

def json_load(file: object) -> str:
    x = file.read().replace('\'', '\"')
    res = json.loads(x)
    return res
# http://stackoverflow.com/questions/18514910/how-do-i-automatically-fix-an-invalid-json-string

def json_save(s: str, file: object) -> None:
    s_n = {'rows':[]}
    if not isinstance(s, str):
        for i in s:
            s_n["rows"].append(i[0])
        json.dump(s_n, file)
    else:
        json.dump(s_n["rows"].append(s), file)

class AbsConverterFabric(ABC):
    @abstractmethod
    def create_converter(self, _from: str, _to: str) -> object:
        raise NotImplemented
class AbstractConverter(ABC):
    @abstractmethod
    def load(self, file: object) -> str:
        raise NotImplemented

    @abstractmethod
    def save(self, s: str, file: object) -> object:
        raise NotImplemented

class ConverterFabric(AbsConverterFabric):
    def create_converter(self, _from: str, _to: str) -> object:
        class Converter(AbstractConverter):
            def __init__(self):
                self._from = _from
                self._to = _to
            def load(self, file: object):
                if self._from ==  'csv':
                    return csv_load(file)
                elif self._from ==  'json':
                    return json_load(file)
                else:
                    print('Function name _from isn\'t corect')

            def save(self, s: str, file: object):
                if self._to == 'csv':
                    return csv_save(s, file)
                elif self._to == 'json':
                    return json_save(s, file)
                else:
                    print('Function name _to isn\'t corect')

        return Converter()

fab = ConverterFabric()
converter1 = fab.create_converter('csv', 'json')
converter2 = fab.create_converter('json', 'csv')

x =  open('csv.txt', 'r')
result = converter1.load(x)
print(result)

print()
y = open('json.txt', 'w')
converter1.save(result, y)

z = open('json.txt', 'r')
result = converter2.load(z)

print(result)

t = open('csv.txt', 'w')
converter2.save(result, t)