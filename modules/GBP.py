import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def GBP():

    dia, mes, ano, date2 = datador.datador('GBP')

    headers = {
        'cookie' : 'ASPSESSIONIDQEDACBAB=OFHNMJBAFOFMLIGHCMHLKLLC; boeconsent=necessary; ASPSESSIONIDQGAABABC=GLEJMCEALBFAONJJGGLNELGF; ASPSESSIONIDCGCDCDCD=IOLNOCEACPCIHGCIIJKOCLBN; ASPSESSIONIDSECCABCA=OLOIADEAOJJOAJNEKHCCHOJP; AKA_A2=A',
        'referer' : 'https://www.bankofengland.co.uk/boeapps/database/Rates.asp?TD=13&TM=Jan&TY=2022&into=GBP&rateview=D',
        'sec-ch-ua' : '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile' : '?0',
        'sec-ch-ua-platform' : 'Windows',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user' : '1',
        'upgrade-insecure-requests' : '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    payload = {
        'TD' : dia,
        'TM' : mes,
        'TY' : ano,
        'into' : 'GBP',
        'rateview' : 'D'
    }

    url = f'https://www.bankofengland.co.uk/boeapps/database/Rates.asp?TD={dia}&TM={mes}&TY={ano}&into=GBP&rateview=D'

    res = requests.get(url, data=payload, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')


    # estrutura de repetição para capturar o valor de taxa do html.


    cont = 0
    rel = 0
    list = []

    for i in soup.find('table').findAll('td'):
        cont += 1
        print(i.get_text())
        if i.get_text() == 'US Dollar':
            rel = cont + 1
        elif cont == rel:
            list.append(i.get_text())

    temp = list
    temp = str(temp).replace('\\n', '')
    temp = str(temp).replace('\\t', '')
    temp = str(temp).replace('\\r', '')
    temp = str(temp).replace(' ', '')
    temp = str(temp).replace('.', ',')
    temp = str(temp[2:8])

    return temp, date2