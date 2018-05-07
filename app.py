from flask import Flask, render_template, request, redirect
from db import *
import sys
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    http_accept = http_accept.replace(';', '; ').replace(',', ', ')
    user_agent = request.headers['User-Agent']
    return render_template('index.html', **locals())

@app.route('/results', methods = ['POST','GET'])
def results():
    if request.method == 'POST':
        data = request.get_json()
        platform = data['platform']
        screen = data['screen']
        lang = data['lang']
        time = data['time']
        touch = data['touch']
        cookie = data['cookie']
        fonts = data['fonts']
        canvas = data['canvas']
        webgl = data['webgl']
        hashVal = data['hash']
        
        
        hvs  = readHash()
        hvs = [i[0] for i in hvs]
        
        if hashVal not in hvs:
            ids = readID()
            if len(ids) == 0:
                idVal = 0
            else:
                ids = [i[0] for i in test]
                idVal = max(ids)+1
            addRow2(idVal,platform,screen,lang,time,touch,cookie,fonts,canvas,webgl,hashVal)
            return '{"visitor":' + str(idVal) + ' }'
        else:
            idVal = readFromHash(hashVal)[0][0]

            return '{"visitor":' + str(idVal) + ' "You have been here before" }'
if __name__=='__main__':
    app.run(debug=True)
