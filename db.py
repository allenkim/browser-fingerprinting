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


