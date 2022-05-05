import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def GTQ():

    dia, mes, ano, date2 = datador.datador('GTQ')

    headers = {
        'cookie' : 'ASPSESSIONIDQESARSCS=ABKHPICABHGJEDIFOJHFGPDG',
        'referer' : 'https://www.banguat.gob.gt/cambio/default.asp',
        'sec-ch-ua' : '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile' : '?0',
        'sec-ch-ua-platform' : 'Windows',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user' : '?1',
        'upgrade-insecure-requests' : '1',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    payload = {
            'kmoneda' : '02',
        'ktipo' : '5',
        'kdia' : dia,
        'kmes' : mes,
        'kanio' : ano,
        'kdia1' : dia,
        'kmes1' : mes,
        'kanio1' : ano,
        'submit1' : 'Consultar'
        }

    url = f'https://www.banguat.gob.gt/cambio/historico.asp?kmoneda=02&ktipo=5&kdia={dia}&kmes={mes}&kanio={ano}&kdia1={dia}&kmes1={mes}&kanio1={ano}&submit1=Consultar'

    res = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    temp = soup.find('td', {'align' : 'right'}).get_text().replace('.',',')

    return temp.strip(), date2