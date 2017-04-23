import re, json, asyncio, aiohttp, psycopg2
from lxml import html

# {
# ‘title’: ‘commodore 64’,
# ‘url’: ‘http://forum.overclockers.ua/viewtopic.php?f=26&t=99999’,
# ‘author’: ‘Amigo77’,
# ‘text’: ‘Selling retro PC –Commodore 64. Buy now price – 100 usd’,
# ‘price’: ‘100’,
# ‘currency’: ‘usd’
# }

async def get_page(url):
    async with session.get(url) as response:
        if response.status == 200:
            page = await response.text()
            return page


def close_db(cur, conn):
    conn.commit()
    cur.close()
    session.close()
    conn.close()


def parse_page(first_page: int, last_page: int):
    list_urls = []
    list_of_advert = []
    for i in range((first_page - 1) * 40, last_page * 40, 40):  # формуємо список сторінок, кожна сторінка +40
        list_urls.append('http://forum.overclockers.ua/viewforum.php?f=26&start={0}'.format(i))

    async def parse(page):
        content = await get_page(page)
        root = html.fromstring(content)
        text_topic = root.xpath('//ul[@class="topiclist topics"]/li/dl')  # title, url
        for i in text_topic:  # title
            topic = {}
            topic["title"] = i.xpath('./dt/div/a/text()')[0]
            topic["url"] = 'http://forum.overclockers.ua' + i.xpath('./dt/div/a/@href')[0][1:]
            topic["author"] = i.xpath('./dd/a')[0].text
            list_of_advert.append(topic)
        return list_of_advert

    async def parse_page_asy():
        tasks = [parse(i) for i in list_urls]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            results.append(result)
        return results


    y = event_loop.run_until_complete(parse_page_asy())
    return y


def parse_topic_content(list_of_page_parse: list):
    list_of_advert = []

    async def parse_topick(list_of_page):
        for dict_page in list_of_page:
            page = await get_page(dict_page["url"])
            croot = html.fromstring(page)
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
        return list_of_advert

    async def parse_topick_asy():
        tasks = [parse_topick(i) for i in list_of_page_parse]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            results += result
        return results

    try:
        y = event_loop.run_until_complete(parse_topick_asy())
        return y
    finally:
        event_loop.close()

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession(loop=event_loop)


    conn = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='postgres'")
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    try:
        cur.execute("CREATE TABLE IF NOT EXISTS overclockers (id serial PRIMARY KEY, title CHAR(255), url CHAR(255) UNIQUE, author CHAR(255),"
                    "text text, price CHAR(20), currency CHAR(10) )")
    except:
        print("Data table already exist")

    value = parse_topic_content(parse_page(1,1))
    for i in value:
        link = i['url'].split('&sid')[0]
        print(link)
        cur.execute("INSERT INTO overclockers (title, url, author, text, price, currency) "
                    "VALUES ( %s, %s, %s, %s, %s, %s) ON CONFLICT (url) DO NOTHING;",
                    (i['title'], link, i['author'], i['text'], i['price'], i['currency']))

    close_db(cur, conn)