import string

def like(numbers: str, a_set: str, b_set: str):
    likes = 0
    numbers, a_set, b_set = numbers.split(' '), a_set.split(' '), b_set.split(' ')
    for i in numbers:
        if i in a_set and i not in b_set:
            likes += 1
        elif i in b_set and i not in a_set:
            likes -= 1
    return likes

numbers = '3 2 10 7 5 5 2 1 2'
a = '2 3 7'
b = '5 10 7'
print(like(numbers, a, b))

numbers = '1 4 10 20 1 11 12'
a = '1 4 1 12'
b = '1 12 10 20'
print(like(numbers, a, b))


def fine_print(n: int):
    for i in range(n+1):
        print('%-10d %-10o %-10x %-10s' % (i,i,i,bin(i)))

fine_print(1000)

def decorator(fun:object):
    def wrapper(x, y, **kwargs):
        try:
            return fun(x,y, **kwargs)
        except Exception as err:
            print('Exception occurred in func:', fun.__name__, err)
            print('Input args:', x, y)
            print('Input kwargs:', kwargs)
            return None
    return wrapper


@decorator
def func(x, y, **kwargs):
    return x / y

print(func(10,0,op='division',base=20))

def filter_func(list_email: list):
    def fil_fun(email):
        if '@' in email and len(email.split('@')) == 2 and len(email.split('@')[0]) > 1 and email[
            0] in string.ascii_letters or '_' in email[0] and len(email.split('@')[1].split('.')) > 1:
            for i in email.split('@')[0]:
                if (i not in string.ascii_letters) and (i not in string.digits) and (i not in '_'):
                    return None
            return email

    return list(filter(fil_fun, list_email))

emails = ['abc@gmail.com.ua', '*@ank.com', '_ny@us.gov.us', 'z@b.kk']
print(filter_func(emails))
