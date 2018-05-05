from flask import Flask, render_template, request

app = Flask(__name__)

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    
    DATABASE_URL = 'DATABASE_URL'
def addRow(conn,name):
    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    name = "man"
    cur = conn.cursor()
    cur.execute(sql,(name,))
    conn.comit()
    conn.close()





@app.route('/')
def home():
    addrow('hello')
    http_accept = request.headers['Accept'] # accept-encoding accept-language
    user_agent = request.headers['User-Agent']
    return render_template('index.html', **locals())

if __name__=='__main__':
    app.run(debug=True)
