import os
import psycopg2

try:
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    
    DATABASE_URL = 'DATABASE_URL'
def addRow(name):
    
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    cur = conn.cursor()
    cur.execute(sql,(name,))
    conn.commit()
    conn.close()

def addRow2(plat,screen,lang,time,touch,cookie,font,canvas,web):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = """INSERT INTO Data(platform,screen,lang,time,touch,cookie,fonts,canvas,webgl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur = conn.cursor()
    cur.execute(sql,(platform,screen,lang,time,touch,cookie,font,canvas,web,))
    conn.commit()
    conn.close()


    
