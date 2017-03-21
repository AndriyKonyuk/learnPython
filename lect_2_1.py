# def pretty_func():
#     print('Some useful message')
#
#
# def do_things(self):
#     print(self.var)
#
#
# class PublicMeta(type):
#     def __new__(meta, name, bases, attrs):
#         for key, value in attrs.items():
#             if not callable(value) and key[:4] == '_' + name + '__' and key[-2:] != '__':
#                 attrs[key[4:]] = value
#                 attrs.pop(key)
#         attrs['pretty_func'] = pretty_func
#         attrs['do_things'] = do_things
#         return type.__new__(meta, name, bases, attrs)
#
#
# class A(metaclass=PublicMeta):
#     __var = 10
#     __df = 78
#
#     def __a(self):
#         print('function __a')
#
#     def __init__(self, x):
#         self.x = x

