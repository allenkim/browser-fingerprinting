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

def addRow2(idV,plat,screen,lang,time,touch,cookie,font,canvas,web,hashV):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    sql = """INSERT INTO Data(id,platform,screen,lang,time,touch,cookie,fonts,canvas,webgl,hash) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur = conn.cursor()
    cur.execute(sql,(idV,plat,screen,lang,time,touch,cookie,font,canvas,web,hashV))
    conn.commit()
    conn.close()

def readAll():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Data""")
    data = cur.fetchall()
    conn.close()
    return data

def readID():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("""SELECT id FROM Data""")
    data = cur.fetchall()
    conn.close()
    return data

def readHash():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute("""SELECT hash FROM Data""")
    data = cur.fetchall()
    conn.close()
    return data

def readFromHash(h):
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    sql = """SELECT id FROM Data WHERE hash = %s"""
    cur.execute(sql,(h,))
    data = cur.fetchall()
    conn.close()
    return data







    
