from flask import Flask,redirect,render_template,request
import pymysql
import datetime
conn = pymysql.connect(host="localhost" , user='root' , password='' , database='cms')

def attendance_add(req):
    
    attendeeType=req.form.get("attendeeType")
    attendee_id=int(req.form.get("attendeeId"))
    type=req.form.get("type")
    flag=0

    time=datetime.datetime.now()

    with conn.cursor() as cur:
        if attendeeType == "student":
            sql="select * from students where student_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "teacher":
            sql="select * from teachers where teacher_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "staff":
            sql="select * from staff where staff_id =%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    if flag==1:
        if type=="in":
            with conn.cursor() as cur:
                sql="""INSERT INTO attendance(attendee_type,attendee_id,timing_in) 
                        Values(%s,%s,%s)"""
                values=(attendeeType,attendee_id,time)
                cur.execute(sql,values)

        else:
            with conn.cursor() as cur:
                sql="""INSERT INTO attendance(attendee_type,attendee_id,timing_out) 
                        Values(%s,%s,%s)"""
                values=(attendeeType,attendee_id,time)
                cur.execute(sql,values)
        return 1


    else:
        return 0
    


def attendance_update(id):
   

    
    
    attendeeType=request.form.get("attendeeType")
    attendee_id=int(request.form.get("attendeeId"))
    type=request.form.get("type")
    flag=0

    time=datetime.datetime.now()

    with conn.cursor() as cur:
        if attendeeType == "student":
            sql="select * from students where student_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "teacher":
            sql="select * from teachers where teacher_id=%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    with conn.cursor() as cur:
        if attendeeType == "staff":
            sql="select * from staff where staff_id =%s"
            data=(attendee_id)
            status= cur.execute(sql,data)
            if status:
                flag=1

    if flag==1:
        if type=="in":
            with conn.cursor() as cur:
                sql="""UPDATE  attendance SET attendee_type=%s,attendee_id=%s,timing_in=%s WHERE attendance_id=%s"""
                values=(attendeeType,attendee_id,time,id)
                cur.execute(sql,values)
                conn.commit()

        else:
            with conn.cursor() as cur:
                sql="""UPDATE attendance SET attendee_type=%s,attendee_id=%s,timing_out=%s  WHERE attendance_id=%s"""
                values=(attendeeType,attendee_id,time,id)
                cur.execute(sql,values)
                conn.commit()
        return 1


    else:
        return 0
    



