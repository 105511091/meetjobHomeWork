# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:48:37 2022

@author: User
"""

import requests
from bs4 import BeautifulSoup

import db

url="https://www.mcdonalds.com/tw/zh-tw.html"

payload={'p':'書籍'}

data=requests.get(url).text

soup=BeautifulSoup(data,'html.parser')

goods=soup.find_all()

cursor=db.conn.cursor()

for row in goods:
    link=row.find('a').get('href')
    photo=row.find('img').get('srcset')
    title=row.find('span',class_='BaseGridItem__title___2HWui').text
    price=row.find('em').text
    price=price.replace('$','').replace(',','')
    
    photos=photo.split()[0]
    
    print(link)
    print(photos)
    print(title)
    print(price)
    print()
    #手機 類別為1
    #要新增時，請先確認 itemtype 的類別，才開始建立資料
    sql="select * from product where name='{}' and itemtype=7".format(title)
    
    cursor.execute(sql)
    db.conn.commit()
    
    if cursor.rowcount == 0: #表示沒該產品
        sql="insert into product(itemtype,name,price,link,photo_url) values('7','{}','{}','{}','{}')".format(title,price,link,photos)
        cursor.execute(sql)
        db.conn.commit()
    
db.conn.close() 