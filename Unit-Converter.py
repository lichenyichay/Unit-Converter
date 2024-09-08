# Author:Chay
# Time:2024/6/4 22:09
# Release:Alpha 1.0.0

from tkinter import *
from UnitConvertChay import *
top = Tk()
top.geometry('750x750')
top.title("单位换算器")
label = Label(text="单位换算器", font=("微软雅黑", 25), anchor="n")
label.pack()

button1=Button(top,text="单位换算")
button1.place(width=200,height=200,x=50,y=200)
button2=Button(top,text="物理量计算")
button2.place(width=200,height=200,x=500,y=200)

top.mainloop()
