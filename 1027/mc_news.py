# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:56:00 2022

@author: User
"""

import requests #上傳用

from bs4 import BeautifulSoup #爬蟲專用

import db

from pymysql.converters import escape_string

url='https://www.mcdonalds.com/tw/zh-tw/newsroom/2022.html'


data=requests.get(url).text


soup=BeautifulSoup(data,'html.parser')

newsitems=soup.find_all('div',class_='cmp-teaser')

cursor=db.conn.cursor()

for row in newsitems:
    
    title=row.find('div',class_='cmp-teaser__title').text
    link=row.find('a').get('href')
    photo=row.get('data-asset')
    modate=row.find('div',class_='cmp-teaser__description').text
    title=escape_string(title)
    
    print(title)
    print(link)
    print(photo)
    print(modate)
    print()
    sql="select * from mc_news where title='{}'".format(title)
    
    cursor.execute(sql)
    db.conn.commit()
    
    
    if cursor.rowcount==0: #查詢的筆數為多少
        sql="insert into mc_news(title,link,photo,modate) values('{}','{}','{}','{}')".format(title,link,photo,modate)
        cursor.execute(sql)
        db.conn.commit()
db.conn.close()
    

