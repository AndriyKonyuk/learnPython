import aiohttp, asyncio, xlsxwriter, re
from lxml import html

HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Host': 'files.coinmarketcap.com',
    'Origin': 'https://coinmarketcap.com',
    'Referer': 'https://coinmarketcap.com/all/views/all/',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'
}


async def get_url(event_loop):
    async with aiohttp.ClientSession(loop=event_loop) as session:
        async with session.get('https://coinmarketcap.com/all/views/all/') as response:
            if response.status == 200:
                return await response.text()


loop = asyncio.get_event_loop()
run = loop.run_until_complete(get_url(loop))

root = html.fromstring(run)
table = root.xpath("//table[@id='currencies-all']")

table_head = tuple(table[0].xpath('./thead/tr/th/text()'))
table_body = table[0].xpath('./tbody/tr')

with xlsxwriter.Workbook("coin_market_cap.xlsx") as workbook:
    bold = workbook.add_format({"bold": True})
    money_format = workbook.add_format({'num_format': '$ ###,###,###,###'})
    money_float_format = workbook.add_format({'num_format': '$ ###,###,###,###.######'})
    money_without_dollar_format = workbook.add_format({'num_format': '###,###,###,###.###'})
    percent_format = workbook.add_format({'num_format': '###,### %'})
    worksheet = workbook.add_worksheet()

    worksheet.add_table('A0:J823')
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 6, 16)
    worksheet.set_column(1, 6, 16)
    worksheet.set_column(7, 9, 8)
    worksheet.write_row(0, 0, table_head, bold)

    row = 1
    col = 0

    for i in table_body:
        _ = [re.sub(r'\s+', '', i) for i in i.xpath('./td/descendant-or-self::text()')]
        v = [i for i in _ if i and i != '*' and i != '**']
        val = [z.replace('?', '00').replace('LowVol', '00') for z in v]
        worksheet.write_number(row, col, int(val[0]))
        worksheet.write(row, col + 1, val[1])
        worksheet.write(row, col + 2, val[2])
        worksheet.write_number(row, col + 3, int(val[3][1:].replace(',','')), money_format)
        worksheet.write(row, col + 4, float(val[4][1:]), money_float_format)
        worksheet.write(row, col + 5, float(val[5].replace(',','')), money_without_dollar_format)
        worksheet.write(row, col + 6, int(val[6][1:].replace(',', '')), money_format)
        worksheet.write_number(row, col + 7, float(val[7][:-1]), percent_format)
        worksheet.write_number(row, col + 8, float(val[8][:-1]), percent_format)
        worksheet.write(row, col + 9, float(val[9][:-1]), percent_format)
        row += 1
