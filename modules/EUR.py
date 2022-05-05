import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def EUR():
    url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html'

    date, date2, datetrad = datador.datador('EUR')

    resp = requests.post(url)

    # estrutura de repetição para capturar o valor de taxa do html.

    soup = BeautifulSoup(resp.content, 'html.parser')

    test = soup.find('table', {'summary': f'Reference rates: {datetrad}'})

    print(test)

    temp = ''

    cont = 0

    result = ''

    print(f'Data: {date}')

    for i in test.findAll('td'):
        temp = i.get_text()
        print(temp)
        if date <=9:
            try: 
                if int(temp[0]) == date:
                    print(f'TEMP: {temp[0]}')
                    result = temp[-6:]
                    break
            except:
                pass

        elif date >=10:
            try:
                if int(temp[:2]) == date:
                    result = temp[-6:]
                    break
            except:
                pass    
        cont += 1
        
    result = str(result).replace('.', ',')

    return result, date2
