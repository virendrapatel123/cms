from flask import Flask,redirect,render_template,request
import pymysql
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def course_add(req):
   
    name=req.form.get("name")
    duration=req.form.get("duration")
    fees=req.form.get("fee")

    with conn.cursor() as cur:
        sql="INSERT into courses(name,duration,fees) values(%s,%s,%s)"
        values=(name,duration,fees)
        cur.execute(sql,values)

    return 1