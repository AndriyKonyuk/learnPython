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
list_of_advert = []

async def parse_page_content(list_of_page: list):
    list_of_advert = []
    f = open('object.json', 'w')

    for dict_page in list_of_page:
        croot = html.parse(dict_page["url"])
        text_topic_cont = croot.xpath('//*/div[@class="content"]')[0].xpath('descendant-or-self::text()')
        s = ''
        for i in text_topic_cont:
            s += i
        s = re.sub(r'\n', '', s)
        dict_page["text"] = s
        r = re.compile(r'(\d+\sгрн|\d+грн|\d+\s\$|\d+\$|\d+\susd|\d+usd|\d+\sруб|\d+руб)')
        price_currency = re.findall(r, s)  # price and currency together
        if price_currency:
            price_currency = price_currency[0]
            price = re.findall(r'\d+', price_currency)[0]
            currency = re.sub(r'\s', '', price_currency.replace(price, ''))
            dict_page["price"] = price
            dict_page["currency"] = currency
        else:
            dict_page["price"] = 'None'
            dict_page["currency"] = 'None'

        list_of_advert.append(dict_page)
    json.dump(list_of_advert, f)
    return 'Parse page content function done'




async def parse_page(first_page: int, last_page: int):

    for i in range((first_page - 1) * 40, last_page * 40, 40):  # формуємо список сторінок, кожна сторінка +40
        root = html.parse('http://forum.overclockers.ua/viewforum.php?f=26&start={0}'.format(i))
        text_topic = root.xpath('//ul[@class="topiclist topics"]/li/dl/dt/div/a')  # title, url

        for i in text_topic:  # title
            ob_json = {}
            ob_json["title"] = i.text
            ob_json["url"] = 'http://forum.overclockers.ua/' + i.attrib['href']
            ob_json["author"] = i.xpath('./../../../dd/a')[0].text
            list_of_advert.append(ob_json)
    return 'Pare page function done'

async def example():
    tasks = [parse_page(0,5), parse_page_content(list_of_advert)]
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        r = event_loop.run_until_complete(example())
        print(r)
    finally:
        event_loop.close()

