from abc import ABC, abstractmethod
import csv
import json


def csv_load(file: object) -> str:
    s = csv.reader(file, delimiter=' ', quotechar='|')
    return s


def csv_save(s: str, file: object) -> None:
    spamwriter = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(s)


def json_load(file: object) -> str:
    res = json.loads(file)
    return res
# http://stackoverflow.com/questions/18514910/how-do-i-automatically-fix-an-invalid-json-string

def json_save(s: str, file: object) -> None:
    while True:
        try:
            json.dump(s, file)
            break
        except Exception as a:
            print(a)

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
f = open('test.txt', 'w')
fab = ConverterFabric()

converter1 = fab.create_converter('csv', 'json')

converter2 = fab.create_converter('json', 'csv')

string = 'Joe Doe Green 77'

with open('json.txt', 'w') as file:
    converter1.save(string, file)

with open('json.txt', 'r') as file:
    result = converter2.load(file)
    print(result)

with open('csv.txt', 'w') as file:
    converter2.save(result, file)