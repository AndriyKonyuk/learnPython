import re

x = 'afoot, catfoot, dogfoot, fanfoot, foody, foolery, foolish, fooster, footage, foothot, footle, footpad, footway, ' \
    'hotfoot, jawfoot, mafoo, nonfood, padfoot, prefool, sfoot, unfool'

y = 'Atlas, Aymoro, Iberic, Mahran, Ormazd, Silipan, altered, chandoo, crenel , crooked, fardo, folksy, forest, ' \
    'hebamic, idgah, manlike, marly, palazzo, sixfold, tarrock, unfold'

r = re.compile(r'(\w*foo\w*)')

print(re.findall(r, x))
print(re.findall(r, y))
print(re.findall(r, x) == x.split(', '))
