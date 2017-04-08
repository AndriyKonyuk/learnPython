def do_things(self):
    print(self.var)

def pretty_func():
    print('Some useful message')

class PublicMeta(type):
    def __new__(meta, name, bases, attrs, **kward):
        patern = '_' + name + '__'
        newattr = {}
        for key, value in attrs.items():
            if not callable(value) and key.startswith(patern) and key[-2:] != '__':
                newattr[key.replace(patern, '')] = value
            else:
                newattr[key] = value
        newattr['pretty_func'] = pretty_func
        newattr['do_things'] = do_things
        return type.__new__(meta, name, bases, newattr, **kward)

class A(metaclass=PublicMeta):
    __var = 10
    __df = 78

    def __a(self):
        print('function __a')

    def __init__(self, x):
        self.x = x
        self.var = 78

x = A(5)
print(x.do_things())