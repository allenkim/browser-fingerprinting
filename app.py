from flask import Flask, render_template, request, redirect
from db import *
import sys
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    try:
        addRow('hello')
    except:
        pass

    test = ['hello']
    http_accept = request.headers['Accept'] # accept-encoding accept-language
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
        try:
            test = readID()
            if len(test) == 0:
                idVal = 0
            else:
                test = [i[0] for i in test]
                idVal = max(test)+1
            addRow2(idVal,platform,screen,lang,time,touch,cookie,fonts,canvas,webgl)
        except:
            pass
    try: 
        test = readID()
        test = [i[0] for i in test]
    except:
        test = ['bye']
    return '{"visitor": 1}'

if __name__=='__main__':
    app.run(debug=True)
