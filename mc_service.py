# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:49:04 2022

@author: User
"""

import requests
from bs4 import BeautifulSoup

import db

url="https://www.mcdonalds.com/tw/zh-tw/full-menu/snacks.html"


data=requests.get(url).text

soup=BeautifulSoup(data,'html.parser')

goods=soup.find_all('li','cmp-category__item')



cursor=db.conn.cursor()

for row in goods:
    link=row.find('a').get('href')
    photo_url=row.find('img').get('src')
    title=row.find('div',class_='cmp-category__item-name').text
    
    
    print(title)
    print(link)
    print(photo_url)
    print()
    #sql="select * from mc_service where title='{}' and itemtype=5".format(title)
    
    #cursor.execute(sql)
    #db.conn.commit()
    
    
    #if cursor.rowcount == 0:
        #sql="insert into mc_service(itemtype,title,link,photo_url) values('5','{}','{}','{}')".format(title,link,photo_url)
        #cursor.execute(sql)
        #db.conn.commit()

db.conn.close() 
 