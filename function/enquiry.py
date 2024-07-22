from flask import Flask,redirect,render_template,request
import pymysql
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')


def enquiry_add(req):

    student_name=req.form.get("studentName")
    father_name=req.form.get("fatherName")
    mother_name=req.form.get("motherName")
    dob=req.form.get("dob")
    address=req.form.get("address")
    mobile=req.form.get("mobile")
    email=req.form.get("email")
    course=req.form.get("course")



    with conn.cursor() as cur:
        sql= """INSERT into enquiry_forms(student_name,father_name,mother_name,dob,address,mobile,email,course)
                values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        values=(student_name,father_name,mother_name,dob,address,mobile,email,course)
        cur.execute(sql,values)

    return 1