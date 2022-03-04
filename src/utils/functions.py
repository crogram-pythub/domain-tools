# -*- coding: utf-8 -*-
# functions


def set_window_center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('%dx%d+%d+%d' % (w, h, (sw - w) / 2, (sh - h) / 2 - 50))
    win.update()