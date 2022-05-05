from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from modules import executor, depara, classificador_citi
from modules import ARS, BRL, BOB, CLP, CAD, EUR, GTQ, GBP, UYU, PYG, DOP
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


app = Flask(__name__, static_url_path='',
static_folder='templates')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["UPLOAD_FOLDER"] = 'static/'


@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/arquivos', methods=['GET'])
def lista_arquivos():
    arquivos = []
    for nome_do_arquivo in os.listdir(app.config["UPLOAD_FOLDER"]):
        arquivos.append(nome_do_arquivo)

    return render_template('index_arquivos.html', content=arquivos)


@app.route('/download', methods=['GET'])
def download():
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename='currency_values.xlsx', as_attachment=True)


@app.route('/cambios', methods=['GET'])
def cambios():
    contentcambios = executor.executor()
    return render_template('cambios_tpt.html', tables=[contentcambios.to_html(classes='data')], titles=contentcambios.columns.values)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)