import re
from lxml import html, etree

# f = open('log.txt', 'r')
# r = re.compile(r'\[warn\]\s?([\w\s/.]+)')
#
#
#
# for i in re.findall(r, f.read()):
#     print(i)

# f = open('test.html')

# r = re.compile(r'http[s]?://([\w.]+)')
# print(re.findall(r, f.read()))

root = html.parse('test.html')
el = root.xpath('//a')
for i in el:
    i.set('href', 'www.google.com.ua')

et = etree.E(root)

    # if i[0:7] != 'http://' and i[0:8] != 'https://':
    #     i = 'http://' + i
        # print(i)
