import re

x = 'fu, tofu, snafu'
y = 'futz, fusillade, functional, discombobulated'

r = re.compile(r'(fu\b|\w+fu)')
print(re.findall(r, x))
print(re.findall(r, y))
print(re.findall(r, x) == x.split(', '))
