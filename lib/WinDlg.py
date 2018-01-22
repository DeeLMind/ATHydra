#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32gui

class WinDlg:
    def __init__(self):
        pass
    def __del__(self):
        pass

    __ClassName = 'NULL'
    __TitleName = 'NULL'



















hWnd = win32gui.FindWindow("#32770","ONDragon'Class DLG")
    win32gui.SetDlgItemText()
    if hWnd:
        print left