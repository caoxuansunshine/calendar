#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

def calendar_mysql_connect():
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="mysql",
                         database="calendar_test",
                         charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

def calendar_mysql_close():
    # 关闭数据库连接
    db.close()

def check_date_exists(int_year, int_month, int_day, db, cursor):
    # SQL 查询语句
    sql = "SELECT * FROM CALENDAR WHERE YEAR = '{}' AND MONTH = '{}' AND DAY = '{}'".format(int_year, int_month, int_day)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        flag = 0
        weather = 0
        mood = 0
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            weather = row[3]
            mood = row[4]
            flag = 1

        return flag, weather, mood

    except:
        print("Error: unable to fecth data")

def date_insert_calendar(int_year, int_month, int_day, db, cursor):
    # SQL 插入语句
    sql_insert = "INSERT INTO CALENDAR(YEAR, MONTH, DAY, WEATHER, MOOD) VALUES ('{}', '{}', '{}', 0, 0)".format(int_year, int_month, int_day)
    try:
        cursor.execute(sql_insert)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

def date_update_calendar(int_year, int_month, int_day, weather, mood, db, cursor):
    # SQL 更新语句
    print("update", int_year, int_month, int_day, weather, mood)
    sql_update = "UPDATE CALENDAR SET WEATHER = '{}', MOOD = '{}' WHERE YEAR = '{}' AND MONTH = '{}' AND DAY = '{}'".format(weather, mood, int_year, int_month, int_day)
    try:
        cursor.execute(sql_update)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

'''
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS CALENDAR")

# 使用预处理语句创建表
sql_create = """CREATE TABLE CALENDAR (
             YEAR INT NOT NULL,
             MONTH INT NOT NULL,
             DAY INT NOT NULL,  
             WEATHER INT,
             MOOD INT )"""

cursor.execute(sql_create)

# SQL 插入语句
sql_insert = """INSERT INTO CALENDAR(YEAR, MONTH, DAY, WEATHER, MOOD)
             VALUES (2020, 2, 28, 3, 1)"""
try:
    cursor.execute(sql_insert)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# SQL 更新语句
sql = "UPDATE CALENDAR SET WEATHER = 4 WHERE YEAR = 2020 AND MONTH = 5 AND DAY = 28"
try:
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# SQL 查询语句
sql = "SELECT * FROM CALENDAR WHERE YEAR = 2020 AND MONTH = 2 AND DAY = 28"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        weather = row[3]
        mood = row[4]
    print(results, weather, mood)

except:
    print("Error: unable to fecth data")
'''


