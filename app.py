from flask import Flask, render_template, request
from db import *
import sys
import json

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
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
            print('hi')
            #addRow2(platform,screen,lang,time,touch,cookie,fonts,canvas,webgl)
        except:
            pass
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    user_agent = request.headers['User-Agent']
    try: 
        test = readAll()
    except:
        test = ['hello']
    return render_template('index.html', **locals())


if __name__=='__main__':
    app.run(debug=True)
