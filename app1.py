import pymysql

conn=pymysql.connect(host="localhost",user="root",password="",database="cms")

def data_get():
    with conn.cursor() as cur:
        sql="select * from students;"
        cur.execute(sql)
        conn.commit()
        data=cur.fetchall()
    return data