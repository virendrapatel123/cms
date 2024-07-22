from flask import Flask,redirect,render_template,request
import pymysql
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')
def teachers_add(req):
    
    first_name=req.form.get("first_name")
    last_name=req.form.get("last_name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    qualification=req.form.get('qualification')
    timing=req.form.get("timing")
    course=req.form.get("course")
    salary=req.form.get('salary')
    date_of_joining=req.form.get("date_of_joining")
    # photo = request.files['photo']
    # photo.save('image/ ' + photo.filename)
    # path='image/ ' + photo.filename


    with conn.cursor() as cur:
        sql="""INSERT into teachers ( first_name, last_name, father_name, mother_name, dob,address,qualification,timing,course,salary,date_of_joining)
                 values(%s, %s, %s, %s, %s, %s,  %s, %s, %s, %s,%s)"""
        values = (first_name, last_name, father_name, mother_name, dob,address, qualification,timing,course,salary,date_of_joining)
        cur.execute(sql,values)
    return 1
        