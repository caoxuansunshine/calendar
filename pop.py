#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import store
import mysql80

def show_today_status(top_frame):
    label_frame = LabelFrame(top_frame, text='show')
    label_frame.grid(column=0, row=5, padx=5, pady=5)
    showinfo = StringVar()
    info = Label(label_frame, textvariable=showinfo)
    info.grid(column=0, row=0, padx=5, pady=5)
    showinfo.set("#color")

    data = [{"time": "2020-02-18"},
            {"time": "2020-02-19"},
            {"time": "2020-02-20"}]
    store.json_write(data)

def set_today_status(int_year, int_month, int_day, db, cursor):
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

    button = Button(action_label_frame, text="confirm", width=10)
    button.grid(row=1, column=1)

    button = Button(action_label_frame, text="cancel", width=10)
    button.grid(row=1, column=2)

    # cal_weather_sunny = Button(top_frame, command=lambda: func_showinfo(top_frame), text="sunny", width=10)
