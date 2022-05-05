from datetime import datetime, date, timedelta


def datador(currency):

    weekday = datetime.today()
    weekday = weekday.strftime('%A')
    date = datetime.today() - timedelta(1)

    semana = ['Tuesday', 'Wednesday', 'Thursday', 'Friday']

    if weekday in semana:
        pass
    if weekday == 'Saturday':
        date = date - timedelta(1)
    if weekday == 'Sunday':
        date = date - timedelta(2)
    if weekday == 'Monday':
        date = date - timedelta(3)

    date2 = date = date.replace(hour=00, minute=00, second=0, microsecond=0)
    
    if currency == 'ARS':
        date = date.strftime('%Y-%m-%d')

    elif currency == 'BRL':
        date = datetime.today() - timedelta(1)
        date = date.strftime('%d/%m/%Y')

    elif currency == 'BOB':
        mes = date.strftime('%m')
        date = date.strftime('%#d')
        print(f'Data BOB Datador {date}')
        print(f'Mes BOB Datador {mes}')
        return date2, date, mes

    elif currency == 'CLP':
        dia = date.strftime('%d')
        mesinter = date.strftime('%m')
        mes = date.strftime('%m')
        mes = mes[1]
        ano = date
        ano = ano.strftime('%Y')
        return date2, date, dia, mesinter, mes, ano
    
    elif currency == 'CAD':
        return date2
    
    elif currency == 'EUR':
        datetrad = date.strftime('%b')
        date = int(date.strftime('%d'))
        return date, date2, datetrad

    elif currency == 'GTQ':
        dia = date
        dia = dia.strftime('%d')
        mes = date
        mes = date.strftime('%m')
        mes = mes[1]
        ano = date
        ano = ano.strftime('%Y')
        return dia, mes, ano, date2

    elif currency == 'GBP':
        dia = date.strftime('%d')
        mes = date.strftime('%b')
        ano = date.strftime('%Y')
        return dia, mes, ano, date2

    elif currency == 'UYU':
        date = date.strftime('%d/%m/%Y')
        return date, date2
    
    elif currency == 'PYG':
        date = date.strftime('%d/%m/%Y')
        return date, date2

    elif currency == 'DOP':
        
        mes = date.strftime('%m')
        date = date.strftime('%d')
        date = int(date)
            
        mounth_column = {'01': 'Jan_Venta', '02': 'Fev_Venta', '03': 'Mar_Venta', '04': 'Apr_Venta', '05': 'Mai_Venta',
            '06': 'Jun_Venta', '07': 'Jul_Venta', '08' : 'Aug_Venta', '09' : 'Set_Venta', '10' : 'Out_Venta', '11' : 'Nov_Venta',
            '12' : 'Dez_Venta'}
            
        column = mounth_column[mes]
        print(f'teste {column}')

        return date, date2, column

    else:
        pass

    return date2, date
