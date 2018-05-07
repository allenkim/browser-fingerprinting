from flask import Flask, render_template, request
from db import *
import sys
import json

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
    try:
        addRow('hello')
    except:
        pass

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
        print(platform,screen,lang,time,touch,cookie,fonts,canvas,webgl)
        try:
            addRow2(platform,screen,lang,time,touch,cookie,fonts,canvas,webgl)
        except:
            pass
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    user_agent = request.headers['User-Agent']
    return render_template('index.html', **locals())


if __name__=='__main__':
    app.run(debug=True)
