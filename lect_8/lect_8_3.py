import re, json, asyncio
from lxml import html
# {
# ‘title’: ‘commodore 64’,
# ‘url’: ‘http://forum.overclockers.ua/viewtopic.php?f=26&t=99999’,
# ‘author’: ‘Amigo77’,
# ‘text’: ‘Selling retro PC –Commodore 64. Buy now price – 100 usd’,
# ‘price’: ‘100’,
# ‘currency’: ‘usd’
# }

root = html.parse('http://forum.overclockers.ua/viewforum.php?f=26')
# print(root.xpath('./*[@class=announce]'))
text_topic = root.xpath('//ul[@class="topiclist topics"]/li/dl/dt/div/a') #title, url
aut_topic = root.xpath('//ul[@class="topiclist topics"]/li/dl/dd[@class="author"]/a') #autor

# for i in text_topic: #title
#     print(i.text)

# for i in text_topic: #url
#     print('http://forum.overclockers.ua/' + i.attrib['href'])

# for i in aut_topic: #autor
#     print(i.text)

croot = html.parse('http://forum.overclockers.ua/viewtopic.php?f=26&t=157117')
content_topic = croot.xpath('//div[@id][1]/div[@class="content"]/child::text()')
print(content_topic)