from flask import Flask,redirect,render_template,request
import pymysql

from function.att import attendance_add
from function.course import course_add
from function.enquiry import enquiry_add
from function.guardian import guardian_add
from function.staff import staff_add
from function.student import student_add
from function.teacher import teachers_add







conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/attendancepage")
def attendancepage():
    return render_template("attendence.html")


@app.route("/coursepage")
def coursepage():
    return render_template("course.html")

@app.route("/enquirypage")
def enquirypage():
    return render_template("enquiryform.html")

@app.route("/staffpage")
def staffpage():
    return render_template("staff.html")

@app.route("/studentpage")
def studentpage():
    return render_template("student.html")

@app.route("/teacherpage")
def teacherpage():
    return render_template("teacher.html")
@app.route("/guardianpage")
def guardianpage():
    return render_template("guardian.html")


@app.route('/attendance', methods=["POST"])
def attendance():
    
    status= attendance_add(request)

    if status==1:
        return redirect("/attendancetable") 
    

    else:
            
        return "INVALID"
        


@app.route('/course', methods=["POST"])
def course():
   status=course_add(request)
   if status==1:
    
        return redirect("/coursetable")

@app.route('/enquiry', methods=["POST"])
def enquiry():
    
    status=enquiry_add(request)

    if status==1:
        return redirect("/enquirytable")

  
@app.route('/guardian', methods=["POST"])
def guardian():
   status=guardian_add(request)
   if status==1:
        return redirect("/guardiantable")


@app.route('/staff', methods=["POST"])
def staff():
    
    status=staff_add(request)
    
    if status== 1:
        return redirect("/stafftable")
    
   

@app.route('/student', methods=["POST"])
def student():
   
    status=student_add(request)
    if status==1:
        return redirect("/studenttable")
  
@app.route('/teachers', methods=["POST"])
def teachers():
   status=teachers_add(request)
   if status==1:
    
    return redirect("/teachertable")

@app.route("/attendancetable")
def attendencetable():
    with conn.cursor() as cur:
        sql="select * from attendance"
        cur.execute(sql)
        data=cur.fetchall()
    

    return render_template("attendencetable.html",datas=data)



@app.route("/coursetable")
def coursetable():

    with conn.cursor() as cur:
        sql="select * from courses"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("coursetable.html" ,datas=data)


@app.route("/enquirytable")
def enquirytable():
    with conn.cursor() as cur:
        sql="select * from enquiry_forms"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("enquirytable.html" ,datas=data)

@app.route("/guardiantable")
def guardiantable():
    with conn.cursor() as cur:
        sql="select * from guardians"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("guardiantable.html" ,datas=data)

@app.route("/stafftable")
def stafftable():
    with conn.cursor() as cur:
        sql="select * from staff"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("stafftable.html" ,datas=data)

@app.route("/studenttable")
def studenttable():
    with conn.cursor() as cur:
        sql="select * from students"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("studenttable.html" ,datas=data)

@app.route("/teachertable")
def teachertable():
    with conn.cursor() as cur:
        sql="select * from teachers"
        cur.execute(sql)
        data=cur.fetchall()
    return render_template("/teachertable.html" ,datas=data)

@app.route("/delete/<id>")
def attendencedelete(id):
   
    with conn.cursor() as cur:
        sql="delete from attendance where attendance_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/attendancetable")
    

    
@app.route("/delete/<id>")
def  coursedelete(id):
   
    with conn.cursor() as cur:
        sql="delete from courses where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/coursetable")
    
@app.route("/delete/<id>")
def  enquirydelete(id):
   
    with conn.cursor() as cur:
        sql="delete from enquiry_forms where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/enquirytable")

@app.route("/delete/<id>")
def  guardiandelete(id):
   
    with conn.cursor() as cur:
        sql="delete from guardians where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/guardiantable")

@app.route("/delete/<id>")
def  staffdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from staff where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/stafftable")

@app.route("/delete/<id>")
def  studentdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from students where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/studenttable")

@app.route("/delete/<id>")
def  teacherdelete(id):
   
    with conn.cursor() as cur:
        sql="delete from teachers where class_id=%s"
        values=(id)

        cur.execute(sql,values)
        return redirect("/teachertable")




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)



