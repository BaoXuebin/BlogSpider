# -*- coding:utf-8 -*-
# python3 对于 mysql 的操作，主要是存储操作
import pymysql
import uuid
import datetime
import json
import os

params = {}
try:
    print(os.getcwd())
    with open('DB.json', 'r') as ff:
        params = json.load(ff)
except:
    pass

formatters = ['%Y-%m-%d', '%Y年%m月%d日', '%Y-%m-%d %a.']

def str2Datetime(string):
    for formatter in formatters:
        try:
            return datetime.datetime.strptime(string, formatter)
        except:
            pass
    return datetime.datetime.now()

def getConnect():
    return pymysql.connect(host=params.get("host"), port=params.get("port"), user=params.get("user"), password=params.get("password"), db=params.get("db"), charset=params.get("charset"))

def insertByBatch(netBlogs, title, origin):
    db = getConnect()
    for netBlog in netBlogs:
        cursor = db.cursor()
        author = netBlog.get("author") if netBlog.get("author") else ''
        date = str2Datetime(netBlog.get("publishTime"))
        # 构建 sql
        sql = "INSERT INTO net_blog(id, title, href, author, publishTime, origin, originLink) VALUES ('%s', '%s', '%s', '%s', '%s', \"%s\")" % \
                (uuid.uuid1(), netBlog.get("title"), netBlog.get("href"), author, date.strftime('%Y-%m-%d'), title, origin)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print(netBlog.get("title"), '保存失败')
            db.rollback()
    db.close()
        
