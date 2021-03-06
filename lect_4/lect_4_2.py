import requests, threading
from lxml import html
import logging
from concurrent.futures import ThreadPoolExecutor




class Scraper:
    def __init__(self, query, page_from, page_to, limit=2):
        self.query = query
        self.page_from = page_from
        self.page_to = page_to + 1
        self.limit = limit
        self.semaphore = threading.BoundedSemaphore(value=self.limit)

    def __prepare(self):
        HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp, * / *;q = 0.8',
            'Accept-Encoding': 'gzip, deflate, lzma, sdch',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US; q = 0.6, en; q = 0.4',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.olx.ua',
            'Referer': 'https://www.olx.ua/',
            'Save-Data': 'on',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 54.0.2840.99 Safari / 537.36OPR / 41.0.2353.69',
        }
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.log = logging.basicConfig(level=logging.INFO)

    def start(self):
        self.__prepare()
        res = []
        # for i in range(self.page_from, self.page_to):
        #     t = threading.Thread(target=self.crawl, args=(self.get_link(i),))
        #     thread.append(t)
        #     self.notify(self.get_link(i))
        #
        # for t in thread:
        #     t.start()
        #
        # for t in thread:
        #     t.join()
        with ThreadPoolExecutor(2) as executor:
            for i in range(self.page_from, self.page_to):
                t = executor.submit(self.crawl, self.get_link(i)) # створюємо окремий потік для url
                link = self.get_link(i)
                t.add_done_callback(self.notify(link))
                res += t.result()  # t.result() повертає список, тому додаєм до нового
        return res

    def notify(self, url_crawl):
        logging.info('Task done: {0}'.format(url_crawl))

    def get_link(self, page):
        link = 'https://www.olx.ua/chernovtsy/q-{0}/?page={1}'.format(self.query, page)
        return link

    def crawl(self, url):
        resp = self.session.get(url)
        if resp.status_code == 200:
            page = resp.text
            root = html.fromstring(page)
            items = []
            offers = root.xpath('//td[@class="offer "]')
            for offer in offers:
                try:
                    title = offer.xpath('.//div[@class="space rel"]/h3/a/strong/text()')[0]
                    price = offer.xpath('.//td[@class="wwnormal tright td-price"]//p/strong/text()')[0]
                    items.append((title, price))
                except:
                    pass
            return items


scrapper = Scraper('iphone', 1, 4, limit=2)
results = scrapper.start()

for result in results:
    offer, price = result
    print(offer, price)
