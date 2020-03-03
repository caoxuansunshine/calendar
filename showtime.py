#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import time

def time_update(root, set_day, set_time):
    day_info = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    time_info = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
    set_day.set(day_info)
    set_time.set(time_info)
    timer = root.after(1000, lambda: time_update(root, set_day, set_time))

def time_ui(root, frame):
    set_day = StringVar()
    set_time = StringVar()

    day_label = Label(frame, textvariable=set_day)
    day_label.grid(row=1, column=2, padx=5, pady=5)
    time_label = Label(frame, textvariable=set_time)
    time_label.grid(row=2, column=2, padx=5, pady=5)

    time_update(root, set_day, set_time)
