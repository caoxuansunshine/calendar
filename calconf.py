#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import mysql80

def set_today_status(int_year, int_month, year_and_month, db, cursor):
    top = Toplevel()
    top.title('Today Status')
    top.geometry('500x400')

    # weather optional
    weather_label_frame = LabelFrame(top, text='weather')
    weather_label_frame.grid(row=2, column=2, padx=20, pady=30)

    weather_int_var = IntVar()
    weather_int_var.set(1)

    sunny_radio_button = Radiobutton(weather_label_frame, text="sunny", value=1, variable=weather_int_var)
    sunny_radio_button.grid(row=1, column=1)

    rainy_radio_button = Radiobutton(weather_label_frame, text="rainy", value=2, variable=weather_int_var)
    rainy_radio_button.grid(row=1, column=2)

    cloudy_radio_button = Radiobutton(weather_label_frame, text="cloudy", value=3, variable=weather_int_var)
    cloudy_radio_button.grid(row=1, column=3)

    # mood optional
    mood_label_frame = LabelFrame(top, text='mood')
    mood_label_frame.grid(row=3, column=2, padx=20, pady=30)

    mood_int_var = IntVar()
    mood_int_var.set(1)

    happy_radio_button = Radiobutton(mood_label_frame, text="happy", value=1, variable=mood_int_var)
    happy_radio_button.grid(row=1, column=1)

    smooth_radio_button = Radiobutton(mood_label_frame, text="smooth", value=2, variable=mood_int_var)
    smooth_radio_button.grid(row=1, column=2)

    angry_radio_button = Radiobutton(mood_label_frame, text="angry", value=3, variable=mood_int_var)
    angry_radio_button.grid(row=1, column=3)

    # action optional
    action_label_frame = LabelFrame(top, text='action')
    action_label_frame.grid(row=4, column=2, padx=20, pady=30)

    print("toplevel", int_year, int_month, year_and_month, weather_int_var.get(), mood_int_var.get())
    button = Button(action_label_frame, text="confirm",
        command=lambda: mysql80.date_update_calendar(int_year, int_month, year_and_month, weather_int_var.get(), mood_int_var.get(), db, cursor), width=10)
    button.grid(row=1, column=1)

    button = Button(action_label_frame, text="cancel", width=10)
    button.grid(row=1, column=2)

def calendar_refresh(frame, format_ym, int_year, int_month, db, cursor):
    for widget in frame.winfo_children():
        widget.destroy()
    calendar_create(frame, format_ym, int_year, int_month, db, cursor)

def calendar_create(frame, format_ym, int_year, int_month, db, cursor):
    names = locals()

    label_day_str = ["一", "二", "三", "四", "五", "六", "日"]
    for n in range(7):
        names['label_day_' + str(n)] = Label(frame, width=10, text=label_day_str[n])
        names['label_day_' + str(n)].grid(row=0, column=n, padx=5, pady=5)

    for i in range(1, len(format_ym)+1):
        for j in range(7):
            year_and_month = int(format_ym[i-1][j])
            if year_and_month > 0:
                color = "whitesmoke"
                check_flag = 0
                # 查询mysql是否存在该项
                check_flag, weather, mood = mysql80.check_date_exists(int_year, int_month, year_and_month, db, cursor)
                if (check_flag == 1):
                    if (weather == 0) and (mood == 0):
                        color = "whitesmoke"
                    elif (weather == 1) or (mood == 1):
                        color = "lightskyblue"
                    elif (weather == 2) or (mood == 2):
                        color = "salmon"
                    else:
                        color = "mediumpurple"
                else:
                    # 不存在则添加mysql该项
                    mysql80.date_insert_calendar(int_year, int_month, year_and_month, db, cursor)

                names['calendar_button_' + str(i) + '_' + str(j)] = Button(frame, bg=color, text=str(year_and_month),
                    command=lambda: set_today_status(int_year, int_month, year_and_month, db, cursor), width=10)
                # 完成布局
                names['calendar_button_' + str(i) + '_' + str(j)].grid(row=i, column=j, padx=5, pady=5)
