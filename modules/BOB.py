import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def BOB():

    date2, date, mes = datador.datador('BOB')
    print(f'Date Function BOB: {date}')
    numerate_mounth = {'01': '1', '02': '3', '03': '5', '04': '7', '05': '9', '06': '11', '07': '13',

                       '08': '15', '09': '17', '10': '19', '11': '21', '12': '23'}


    url = 'https://www.bcb.gob.bo/tiposDeCambioHistorico/'

    res = requests.post(url, verify=False)

    soup = BeautifulSoup(res.content, 'html.parser')
    num_tag = int(numerate_mounth[mes])

    last_tag = cont = rel = 0

    list = []

    temp = ''

    for i in soup.findAll('td', {'class': 'textoDatos'}):
        print(f'Item: {i.get_text()}, Contador: {cont}')
        cont+=1

        if i.get_text() == date:
            rel = cont + num_tag
            print(f'Indice Tag Resultado: {rel}')

        if cont == rel:
            list.append(i.get_text())

        if i.get_text() == date:
            last_tag = cont + 1

        if last_tag == cont:

            temp = i.get_text()

        else:
            pass

    if list[0] == '\xa0':

        return temp

    else:
        print(f'Result!: {list[0]}')
        return list[0], date2