import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def UYU():

    date, date2 = datador.datador('UYU')

    headers = {
        'Cookie' : 'ckpersistweb-20480=BMBEABAKFAAA; _ga=GA1.3.343961990.1642080869; _gid=GA1.3.916054985.1642080869; WSS_FullScreenMode=false; _gat_gtag_UA_32096954_1=1',
    'Host' : 'www.bcu.gub.uy',
    'If-Modified-Since' : 'Thu, 13 Jan 2022 20:17:22 GMT',
    'sec-ch-ua' : '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile' : '?0',
    'sec-ch-ua-platform' : 'Windows',
    'Sec-Fetch-Dest' : 'document',
    'Sec-Fetch-Mode' : 'navigate',
    'Sec-Fetch-Site' : 'cross-site',
    'Sec-Fetch-User' : '?1',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    #payload = '{"KeyValuePairs":{"Monedas":[{"Val":"0","Text":"TODAS"}],"FechaDesde":"17/01/2022","FechaHasta":"17/01/2022","Grupo":"2"}}'
    payload = f'{{"KeyValuePairs":{{"Monedas":[{{"Val":"0","Text":"TODAS"}}],"FechaDesde":"{date}","FechaHasta":"{date}","Grupo":"2"}}}}'
    url = 'https://www.bcu.gub.uy/_layouts/15/BCU.Cotizaciones/handler/CotizacionesHandler.ashx?op=getcotizaciones'

    res = requests.post(url, data=payload, headers=headers)
    temp = res.json()['cotizacionesoutlist']['Cotizaciones'][0]['TCC']

    return str(temp).replace('.', ','), date2
