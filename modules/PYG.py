import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def PYG():
    
    date, date2 = datador.datador('PYG')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'BNIS_STCookie=24Ir6CarIw2CYox0iECyeR7ZZkPiKsLt9xBzL/DGRBYXClv6jFR70yeFxbOdER7Diur3NCNCM1UBv2qSJCqiYw==; PHPSESSID=5jmju29b6fes6jub6vjql6ac90; _ga=GA1.3.1150475515.1642034021; __utmc=265214748; __utmz=265214748.1642034022.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); x-bni-ja=-414927493; BNIS_x-bni-jas=OPncuXSTrCg60Jqj/iPvK0/xVg+v8KmLZlVI+QS4oA3YQiLCWnWPu7v5qQe3SZrvK2YlSuxLFNsnPTUpwXL5UpZJE8L7JYolK1Zli7/yDi2ANYP5iAYicA==; _gid=GA1.3.1294859818.1642188839; __utma=265214748.1150475515.1642034021.1642091887.1642188839.4; __utmt=1; _gat=1; __utmb=265214748.3.10.1642188839',
        'Host': 'www.bcp.gov.py',
        'Origin': 'https://www.bcp.gov.py',
        'Referer': 'https://www.bcp.gov.py/webapps/web/cotizacion/monedas',
        'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    payload = {
        'fecha': date
    }

    url = 'https://www.bcp.gov.py/webapps/web/cotizacion/monedas'
    res = requests.post(url, data=payload, headers=headers, verify=False)
    soup = BeautifulSoup(res.content, 'html.parser')

    cont = 0
    list = []

    for i in soup.findAll('td', {'style': 'text-align:right'}):
        cont += 1
        if cont == 2:
            list.append(i.get_text())
            temp =str(list[0])
    return temp.replace('.', ','), date2
