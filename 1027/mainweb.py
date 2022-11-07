# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:56:17 2022

@author: User
"""

from flask import Flask,render_template,request,url_for,redirect

import db

app=Flask(__name__)

@app.route('/')
def index():
    

    return render_template("index.html")

@app.route('/contact')
def message():
    return render_template("contact.html")

@app.route("/addMessage",methods=['POST'])
def addContact():
    if request.method =='POST':
        username=request.form.get('username')
        title=request.form.get('title')
        email=request.form.get('email')
        content=request.form.get('content')
        
        sql="insert into mc_message(title,username,email,content) values('{}','{}','{}','{}')".format(title,username,email,content)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
     
    return redirect(url_for('message'))

@app.route('/news')
def news():
    sql="select * from mc_news order by id desc"
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    allnews=cursor.fetchall()
    return render_template("news.html",**locals())
    

@app.route('/service',methods=['GET'])
def service():
    items = request.args.get('item')
    keyword = request.args.get('p')
    #使用者都沒有依條件查詢，只單獨點選產品頁的連結
    if items == None and keyword == None:
        sql="select * from mc_service order by id desc limit 6"
    elif len(items) >0 and len(keyword) == 0:
        #使用者查類別但沒有查關鍵字
        sql=sql="select * from mc_service where itemtype='{}'".format(items)
    elif items == "0" and len(keyword) >0:
        #關鍵字查詢
        sql="select * from mc_service where title like '%{}%'".format(keyword)
    
    else:
        #使用者查類別及關鍵字
        sql="select * from mc_service where itemtype='{}' and title like '%{}%'".format(items,keyword)

    
    cursor=db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res=cursor.fetchall()
    return render_template("service.html",result=res)

@app.route('/about')
def about():
    return render_template("abouts.html")


app.run(debug=True,host='0.0.0.0',port=5555)
