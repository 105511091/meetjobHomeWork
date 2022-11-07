# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:09:32 2022

@author: User
"""

import pymysql

dbsetting ={
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"123456789",
    "db":"flaskweb",
    "charset":"utf8"
    
    }
conn=pymysql.connect(**dbsetting)