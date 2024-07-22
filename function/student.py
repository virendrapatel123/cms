from flask import Flask,redirect,render_template,request
import pymysql
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')


def student_add(req):
   
    first_name=req.form.get("first_name")
    last_name=req.form.get("last_name")
    father_name=req.form.get("father_name")
    mother_name=req.form.get("mother_name")
    dob=req.form.get("dob")
    address=req.form.get("address")
    course=req.form.get("course")
    mobile=req.form.get("mobile")
    email=req.form.get("email")
    photo = req.files['photo']
    photo.save('image/ ' + photo.filename)
    path='image/ ' + photo.filename



    with conn.cursor() as cur:
        sql="INSERT into students (first_name, last_name, father_name, mother_name, dob, address, course, mobile, email, photo) values( %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s)"
        values = ( first_name, last_name, father_name, mother_name, dob, address, course, mobile, email, path)
        cur.execute(sql,values)
        conn.commit()

    return 1