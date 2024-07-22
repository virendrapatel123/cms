from flask import Flask,redirect,render_template,request
import pymysql
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def guardian_add(req):
    guardian_id=req.form.get("guardianID")
    student_id=req.form.get("studentName")
    father_name=req.form.get("fatherName")
    mother_name=req.form.get("motherName")
    address=req.form.get("address")
    mobile=req.form.get("mobile")
    email=req.form.get("email")

    with conn.cursor() as cur:
        sql= """INSERT into guardians(guardian_id,student_id,father_name,mother_name,address,mobile,email)
                values(%s,%s,%s,%s,%s,%s,%s)"""
        values=(guardian_id,student_id,father_name,mother_name,address,mobile,email)
        cur.execute(sql,values)
    return 1
