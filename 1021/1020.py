# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:30:43 2022

@author: User
"""

import db

def employee():
    name=input("請輸入員工姓名:")
    sex=input("請輸入員工性別:")
    tel=int(input("請輸入電話:"))
    assume=input("請輸入到職日期:")

    sql="insert into employee(name,sex,tel,assume) values('{}','{}','{}','{}')".format(name,sex,tel,assume)

    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
#print(employee())
def works():
    item=input("工作項目:")
    info=input("工作內容:")
    employeeid=input("員工編號:")

    sql="insert into works(item,info,employeeid) values('{}','{}','{}')".format(item,info,employeeid)

    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
#print(works())

def update():
    print("修改員工資料")
    
    id=input("請輸入員工編號:")

    sex=input("修改性別:")
    tel=int(input("修改電話:"))
    sql="update employee set sex='{}',tel='{}' where id='{}'".format(sex,tel,id)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
           
#print(update())
def select1():
    print("查詢員工基本資料")
    
    x=input("請輸入員工編號:")
    sql="select * from employee where id='{}'".format(x)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    news=cursor.fetchall()
    return news
#print(select1())

def select2():
    print("查詢員工工作內容")
    
    x=input("請輸入員工編號:")
    sql="select e.name,w.item,w.info from employee e inner join works w on e.id=w.id where w.employeeid='{}'".format(x)
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    news=cursor.fetchall()
    return news
print(select2())
    
    