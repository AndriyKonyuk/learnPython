import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('country_code', metavar='N', type=str, help='country code')
parser.add_argument('-l', type=str, help='name of location')
parser.add_argument('-i', type=int, help='id location')
p = parser.parse_args()

if p.i != None:
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?id={0}&appid=ff9853a87b307198d1cb16c5265804dd'.format(
            p.i))
    r_temp = dict(r.json())['main']['temp'] - 273.15
    s = 'Current temp: {0:.3}{1}C'.format(r_temp, repr('u00B0'))  # xb0
    print(s)
elif p.l != None:
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid=ff9853a87b307198d1cb16c5265804dd'.format(
            p.l, p.country_code))
    r_temp = dict(r.json())['main']['temp'] - 273.15
    s = 'Current temp: {0:.3}{1}C'.format(r_temp, repr('u00B0'))  # xb0  \u2103
    print(s)