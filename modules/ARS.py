import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from modules import datador


def ARS():
    
    date2, date = datador.datador('ARS')

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=272&detalle=Tipo%20de%20Cambio%20Mayorista%20($%20por%20US$)%20Comunicaci%F3n%20A%203500%A0-%20Referencia',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'f5_cspm=1234; ASPSESSIONIDQCCRSTCT=LPMDLLNCBBKADPOMMGEJKKGC; _ga=GA1.3.1160700631.1641925286; _gid=GA1.3.1460742636.1641925286; TS9a50b177027=08403d584cab2000bcb6c329bb29e34911232cd44f3c1dbd08d8e2b890640d47d4683b8d305a2cd908c1712d8a113000fc2a2ea50c76f9bf768a5aebd4f62e5f2c86aaee82b38b26d3c413d86c182234274f071241edef48233e70c8d76a614a; f5avr0049651832aaaaaaaaaaaaaaaa_cspm_=CBKIECCEIKBOKJBGFKDBOKEJFECJEPKKHFMCAAMDMDGHOAIPMKDMPLPHMKLHKLCPGCKCFLKHBJJIPAOJJGJAAEBFANNBIALFLDGLDEJBICPGDHHNHOGLDHGOMIEHDHMF; ASPSESSIONIDSSRDRBDS=MJNIJFOCEEOJNGNDLAHNFPEG; TS015a32b2=01532640e8bce21bb8acff0d142952d0e54ec2d91bf1ad0fc87045567cae4750fdb09c8194958a50975b63b4e66cfe52884e41423a641a4990d7b4f044094505c5e163eeed92dad1c9cd9f6a03acbe9e40f90003ad01bf8799679a11b34317478b10ad615ab3ffabbf894c2d452da55e8304ca7ed3'
    }

    url = 'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables_datos.asp'

    payload = {
        'fecha_desde': date, 'fecha_hasta': date, 'B1': 'Enviar', 'primeravez': '1', 'serie': '272', 'serie1': '0',
        'serie2': '0', 'serie3': '0', 'serie4': '0',
        'detalle': 'Tipo+de+Cambio+Mayorista+%28%24+por+US%24%29+Comunicaci%F3n+A+3500%A0-+Referencia'
    }

    res = requests.post(url, data=payload, headers=headers)

    soup = BeautifulSoup(res.content, 'html.parser')

    cont = 0
    list = []

    for div in soup.findAll('div', {'align': 'right'}):
        cont += 1
        if cont == 16:
            list.append(div.get_text())

    return list[0], date2