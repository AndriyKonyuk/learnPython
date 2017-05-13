# HUEY module
# Celery, jcelery для виконання задачі в циклі + BD Redise
# for flask module eve
# ORM for postgresSQL
# perfech on SQL
# use SQLALchemy
# wtfforms
# pip freeze > requirements.txt

class MDict(dict):
    def __init__(self, mydict, **kwargs):
        super().__init__(mydict, **kwargs)

    def map(self, fun, values=True):
        for k, v in super.myDict.items():
            if values == True:
                super.myDict[k] = fun(super.myDict[k])
            else:
                new_key = fun(k)
                val = super.myDict[k]
                del super.myDict[k]
                super.myDict[new_key] = val


x = MDict({1: 0, 2: 0, 3: 0, 4: 0})
# x = MDict({'a': 0, 'b': 0, 'c': 0, 'd': 0})

x.map(lambda y: y + 1, values=False)
print(x.myDict)
