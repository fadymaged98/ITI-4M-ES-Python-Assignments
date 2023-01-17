from tkinter import *
import tkinter as tk
window_2 = Tk()
window_2.title("Calculator")
window_2.geometry('500x500')
window_2.configure(bg='light blue')

field = Entry(window_2, width=40, font=("Comic Sans MS", 10, "bold"))
field.place(x=80,y=80)
field_txt = ""

def add_to_field(data):
    global field_txt
    field_txt += str(data)
    field.delete("0","end")
    field.insert("0",field_txt)
def calc():
    global field_txt
    res = str(eval(field_txt))
    field.delete("0","end")
    field.insert("0",res)
def clr():
    global field_txt
    field_txt = ""
    field.delete("0", "end")

b0 = Button(window_2, text="0", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(0)).place(x=10, y=400)
b1 = Button(window_2, text="1", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(1)).place(x=50, y=400)
b2 = Button(window_2, text="2", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(2)).place(x=90, y=400)
b3 = Button(window_2, text="3", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(3)).place(x=130, y=400)
b4 = Button(window_2, text="4", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(4)).place(x=50, y=325)
b5 = Button(window_2, text="5", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(5)).place(x=90, y=325)
b6 = Button(window_2, text="6", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(6)).place(x=130, y=325)
b7 = Button(window_2, text="7", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(7)).place(x=50, y=250)
b8 = Button(window_2, text="8", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(8)).place(x=90, y=250)
b9 = Button(window_2, text="9", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='maroon',
            bd='5',command=lambda :add_to_field(9)).place(x=130, y=250)

b_plus = Button(window_2, text="+", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :add_to_field("+")).place(
    x=350, y=370)
b_minus = Button(window_2, text="-", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :add_to_field('-')).place(
    x=300, y=370)
b_multiply = Button(window_2, text="/", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :add_to_field('/')).place(
    x=350, y=262)
b_divide = Button(window_2, text="*", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :add_to_field('*')).place(
    x=300, y=262)
b_equal = Button(window_2, text="=", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :calc()).place(
    x=400, y=370)
b_clr = Button(window_2, text="CLR", width=5, height=5, font=("Comic Sans MS", 10, "bold"), bg='saddlebrown',command=lambda :clr()).place(
    x=400, y=262)


entry1=Entry()
window_2.mainloop()
