import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def BRL():
    
    date2, date = datador.datador('BRL')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '_ga=GA1.3.1857290355.1641574955; _gid=GA1.3.1903456266.1641922709; JSESSIONID=0000SlgIdI4VyHrwk2UXFyeH3D7:1d4qipvod; TS0168a648=0198c2d644439fd3656cf52841a44eea87bdd2c3ce72cd84fb8ec6073f1b3bacf4c680d2371f4c7e276019ef5476459ba0a026d4f7; dtLatC=2; dtPC=-; dtSa=true%7CC%7C-1%7C%5Bperiodicidade%5D%20to%20value%20%5BA%20DEFINIR%5D%7C-%7C1641927692438%7C327676863_409%7Chttps%3A%2F%2Fwww3.bcb.gov.br%2Fsgspub%2Flocalizarseries%2FlocalizarSeries.do%3Fmethod%3DprepararTelaLocalizarSeries%7CSGS%20-%20Sistema%20Gerenciador%20de%20S%C3%A9ries%20Temporais%7C1641927678968%7C; dtCookie=594044B9B28FEA2C152CDD48BA3B7F85|c2dzfDF8X2RlZmF1bHR8MXxwdGF4fDE; TS01d9825e=0198c2d644d907c70c2378b2a672e5b531cdd6f5b7ef7e60d6691c50929128fb0650437f2a34047298896ecd42cf8a986387be8535; TS01a81efb=01aefc75692082897bcace741b625139bb2c43a26a37901b59c5c0d8c616c5c055fa286b67698238cae8522bda7ea5bd59946c76b044b96b75279ab51fd3195e25ee8d61c2a4dea8d272b98f954644a8b75685e8c7',
        'Host': 'ptax.bcb.gov.br',
        'Origin': 'https://ptax.bcb.gov.br',
        'Referer': 'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=exibeFormularioConsultaBoletim',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    url = 'https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim'

    payload = {
        'RadOpcao': '1',
        'DATAINI': '10/12/2021',
        'DATAFIM': date,
        'ChkMoeda': '61',
    }

    test = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(test.content, 'html.parser')
    controle = 0
    cont = 0
    rel = 0
    list = []
    temp = ''

    for i in soup.findAll('td'):
        controle += 1
    print(f'controle é: {controle}')

    for i in soup.findAll('td'):
        cont += 1
        temp = i.get_text()
        if cont < controle - 1:
            if i.get_text() == date:
                rel = cont + 3
            if cont == rel:
                list.append(i.get_text())
        else:
            list.append(i.get_text())

    return list[0], date2