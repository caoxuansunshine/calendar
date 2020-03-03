#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import calendar
import datetime
import calconf
import showtime
import pymysql


def on_closing(db):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # 关闭数据库连接
        db.close()
        root.destroy()

def confirm_ym(combo_year, combo_month, format_ym, db, cursor):
    int_year = int(combo_year.get())
    int_month = int(combo_month.get())
    format_ym = calendar.monthcalendar(int_year, int_month)

    calconf.calendar_refresh(frame, format_ym, int_year, int_month, db, cursor)

if __name__ == '__main__':
    global db
    global cursor
    # 打开数据库连接
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="mysql",
                         database="calendar_test",
                         charset='utf8')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 创建主窗口,用于容纳其它组件
    root = Tk()

    # 给主窗口设置标题内容  
    root.title("Calendar")
    root.geometry('700x500')
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(db))

    # 显示实时时间
    frame_time = Frame(root)
    frame_time.grid(row=0, column=0, padx=5, pady=5)
    showtime.time_ui(root, frame_time)

    # 设置下拉菜单中的值
    current_date = datetime.datetime.now()
    text_year = current_date.year
    text_month = current_date.month
    format_ym = calendar.monthcalendar(text_year, text_month)

    label_frame_ym = LabelFrame(root, text='Year & Month')
    label_frame_ym.grid(row=1, column=0, padx=5, pady=5)

    combo_year = ttk.Combobox(label_frame_ym)
    combo_year['value'] = ('2018', '2019', '2020', '2021', '2022')
    combo_year.set(text_year)
    combo_year.grid(row=0, column=0, padx=5, pady=5)

    combo_month = ttk.Combobox(label_frame_ym)
    combo_month['value'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    combo_month.set(text_month)
    combo_month.grid(row=0, column=1, padx=5, pady=5)

    button_ym = Button(label_frame_ym, command=lambda: confirm_ym(combo_year, combo_month, format_ym, db, cursor), text="Confirm", width=10)
    button_ym.grid(row=0, column=2, padx=5, pady=5)

    # 创建一个查询结果的按钮
    frame = Frame(root)
    frame.grid(row=2, column=0, padx=30, pady=20)

    calconf.calendar_create(frame, format_ym, int(text_year), int(text_month), db, cursor)

    # 主程序执行  
    mainloop()
