import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador

def CLP():

    date2, date, dia, mesinter, mes, ano = datador.datador('CLP')

    esp_meses = {'01' : 'Ene', '02' : 'Feb', '03' : 'Mar', '04' : 'Abr', '05' :  'May', '06' : 'Jun', '07' : 'Jul',
             '08' : 'Ago', '09' : 'Sep', '10' : 'Oct', '11' : 'Nov', '12' : 'Dic'}


    temp = esp_meses[mesinter]
    testrp = dia + f' {temp} ' + ano
    payloadate = ano + '.' + mes + '.' + dia


    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ASP.NET_SessionId=cqff0lgdntdhcoayenx114s0; _ga=GA1.2.22670915.1642020197; _gid=GA1.2.1276717373.1642422757',
        'Host': 'si3.bcentral.cl',
        'Origin': 'https://si3.bcentral.cl',
        'Referer': 'https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx',
        'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    url = 'https://si3.bcentral.cl/indicadoressiete/secure/indicadoresdiarios.aspx'

    r_sess = requests.Session()
    r1 = r_sess.get(url)
    sight = BeautifulSoup(r1.content, 'html.parser')
    viewstate = sight.find('input', {'id' : '__VIEWSTATE'})
    viewstate = str(viewstate)
    viewstate = viewstate.split(' ')
    viewstate = viewstate[-1]
    viewstate = viewstate.replace('value="', '')
    viewstate = viewstate.replace('"/>', '')


    eventvalidation = sight.find('input', {'id' : '__EVENTVALIDATION'})
    eventvalidation = str(eventvalidation)
    eventvalidation = eventvalidation.split(' ')
    eventvalidation = eventvalidation[-1]
    eventvalidation = eventvalidation.replace('value="', '')
    eventvalidation = eventvalidation.replace('"/>', '')

    payload = {
        'h_calendario': f'{payloadate};2022.1.1',
        'sd_calendario': '',
        '__VIEWSTATE': f'{viewstate}',
        '__VIEWSTATEGENERATOR': '1B8F72FA',
        '__EVENTTARGET': 'calendario',
        '__EVENTARGUMENT': '',
        '__EVENTVALIDATION': f'{eventvalidation}',
        'txtDate': testrp
    }


    resp = requests.post(url, data=payload, headers=headers)

    soup = BeautifulSoup(resp.content, 'html.parser')

    list = []

    result = soup.find('label', {'id': 'lblValor1_3'}).get_text()
    list.append(result)

    return list[0], date2