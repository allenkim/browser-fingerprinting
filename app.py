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
        print(request.data)
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    user_agent = request.headers['User-Agent']
    return render_template('index.html', **locals())


if __name__=='__main__':
    app.run(debug=True)
