import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import pandas as pd
import pdfplumber
from modules import datador


def DOP():

    date, date2, column = datador.datador('DOP')

    headers = {
            'cookie': '_ga=GA1.3.1456004261.1642104686; _gid=GA1.3.1529379510.1642760506; _ce.s=v11.rlc~1642770319105; _gat_gtag_UA_121185163_1=1',
            'referer': 'https://www.bancentral.gov.do/',
            'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    payload = {
            'v': '1642770507906'
        }

    url = 'https://cdn.bancentral.gov.do/documents/estadisticas/mercado-cambiario/documents/TAC4009_BC_2022.pdf?v=1642770507906'

    resp = requests.get(url, headers=headers)

    with open('novoarquivo.pdf', 'wb') as novo_arquivo:
        novo_arquivo.write(resp.content)

    pdf = pdfplumber.open('novoarquivo.pdf')
    p = pdf.pages[0]
    tabela = p.extract_table()
    test = pd.DataFrame(tabela)
    test.rename(columns={0: 'Dias', 1: 'Jan_Compra', 2: 'Jan_Venta', 3: 'Feb_Compra', 4: 'Feb_Venta',
                5 : 'Mar_Compra', 6 : 'Mar_Venta', 7 : 'Apr_Compra', 8 : 'Apr_Venta', 9 : 'Mai_Compra',
                10 : 'Mai_Venta', 11 : 'Jun_Compra', 12 : 'Jun_Venta', 13 : 'Jul_Compra', 14 : 'Jul_Venta',
                15 : 'Aug_Compra', 16 : 'Aug_Venta', 17 : 'Set_Compra', 18 : 'Set_Venta', 19 : 'Out_Compra',
                20 : 'Out_Venta', 21 : 'Nov_Compra', 22 : 'Nov_Venta', 23 : 'Dez_Compra', 24 : 'Dez_Venta'}, inplace=True)

    test.drop(test.head(1).index, inplace=True)
    print(test)
    try:
        temp = test[column].iloc[date]
        temp = temp.replace('.', ',')
    
    except (Exception) as err:
        print(err)
        temp = 'ERROR'

    return temp, date2
