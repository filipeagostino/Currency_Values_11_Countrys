import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def CAD():

    date2 = datador.datador('CAD')

    headers = {
        'Cookie': '_ga=GA1.2.38073544.1642077180; _gid=GA1.2.660201449.1642077180; _gat_gtag_UA_18534530_2=1',
        'Host': 'www.bankofcanada.ca',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    url = 'https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/'

    resp = requests.post(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    list = []
    cont = 0
    size = len(soup.findAll('td', {'class': 'bocss-table__td bocss-table__td--data'}))

    for i in soup.findAll('td', {'class': 'bocss-table__td bocss-table__td--data'}):
        cont += 1
        if cont == size:
            list.append(i.get_text())
        else:
            print(i)
    return list[0].replace('.', ','), date2
