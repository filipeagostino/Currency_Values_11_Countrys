import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
from modules import ARS, BRL, BOB, CLP, CAD, EUR, GTQ, GBP, UYU, PYG, DOP


def executor():

    dict = {}
    listmoedas = []
    listvalores = []
    listdates = []
    try:
        testandoars, testandodatesars = ARS.ARS()
        listmoedas.append('ARS')
        listvalores.append(testandoars)
        listdates.append(testandodatesars)
    except:
        listmoedas.append('ARS')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandobrl, testandodatesbrl = BRL.BRL()
        listmoedas.append('BRL')
        listvalores.append(testandobrl)
        listdates.append(testandodatesbrl)
    except:
        listmoedas.append('BRL')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandobob, testandodatesbob = BOB.BOB()
        listmoedas.append('BOB')
        listvalores.append(testandobob)
        listdates.append(testandodatesbob)
    except:
        listmoedas.append('BOB')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandoclp, testandodatesclp = CLP.CLP()
        listmoedas.append('CLP')
        listvalores.append(testandoclp)
        listdates.append(testandodatesclp)
    except:
        listmoedas.append('CLP')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandocad, testandodatescad = CAD.CAD()
        listmoedas.append('CAD')
        listvalores.append(testandocad)
        listdates.append(testandodatescad)
    except:
        listmoedas.append('CAD')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandoeur, testandodateseur = EUR.EUR()
        listmoedas.append('EUR')
        listvalores.append(testandoeur)
        listdates.append(testandodateseur)
    except:
        listmoedas.append('EUR')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandogtq, testandodatesgtq = GTQ.GTQ()
        listmoedas.append('GTQ')
        listvalores.append(testandogtq)
        listdates.append(testandodatesgtq)
    except:
        listmoedas.append('GTQ')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandogbp, testandodatesgbp = GBP.GBP()
        listmoedas.append('GBP')
        listvalores.append(testandogbp)
        listdates.append(testandodatesgbp)
    except:
        listmoedas.append('GBP')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandouyu, testandodatesuyu = UYU.UYU()
        listmoedas.append('UYU')
        listvalores.append(testandouyu)
        listdates.append(testandodatesuyu)
    except:
        listmoedas.append('UYU')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandopyg, testandodatespyg = PYG.PYG()
        listmoedas.append('PYG')
        listvalores.append(testandopyg)
        listdates.append(testandodatespyg)
    except:
        listmoedas.append('PYG')
        listvalores.append('ERROR')
        listdates.append(datetime.today())
    try:
        testandodop, testandodatesdop = DOP.DOP()
        listmoedas.append('DOP')
        listvalores.append(testandodop)
        listdates.append(testandodatesdop)
    except:
        listmoedas.append('DOP')
        listvalores.append('ERROR')
        listdates.append(testandodatesdop)

    dict['Currency'] = listmoedas
    dict['Value'] = listvalores
    dict['Date'] = listdates
    df = pd.DataFrame(dict)
    currency_values = df.copy()
    df= df[['Currency', 'Value']]
    
    print(currency_values)
    currency_values = currency_values[['Date', 'Currency', 'Value']]
    leitura = pd.read_excel('static/currency_values.xlsx')
    
    list_frames = [currency_values, leitura]
    
    concat = pd.concat(list_frames)

    concat.drop_duplicates(subset=['Date', 'Currency', 'Value'], keep='last', inplace=True)

    concat.to_excel('static/currency_values.xlsx', encoding='latin-1', index=False)

    df1 = pd.read_excel('static/currency_values.xlsx')
    df1['Value'] = df1['Value'].astype(str)
    df1['Value'].replace(',', '.', regex=True)
    #df1['Value'] = df1[df1['Value'] != 'ERROR']
    #df = df1[df1[df1['Value'] != 'ND']]
    df1['Date'] = df1['Date'].dt.strftime('%d')
    df1['Date'] = df1['Date'].astype(int)
    print(df1)
    print(df1.info())

    plt.figure(figsize=(10, 10))
    sns.lineplot(data=df1, x='Date', y='Value', hue='Currency')
    plt.savefig('templates/dist/img/currency_values.jpg')

    print(df1)

    
    return df