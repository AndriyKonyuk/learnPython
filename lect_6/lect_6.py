# XPath - путь к елементу к xml, здійснює навігацію по DOM
# / - вибір з корня елементу
# // - всюди по документу
# . -
# .. -
# @ - атрибут
#
#
# все айтеми
#

from lxml import html

root = html.parse('index.html')
print(root.xpath('//item'))

root.xpath('//item')[0].attrib['class'] = 'myclass'

root.xpath('//item').append(html.etree.Element("div"))

print(root.xpath('//item[@id="2"]/p/text()'))
print(root.xpath('//div/a/@href'))


