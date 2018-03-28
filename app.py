from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    user_agent = request.headers['User-Agent']
    return render_template('index.html', **locals())

if __name__=='__main__':
    app.run(debug=True)
