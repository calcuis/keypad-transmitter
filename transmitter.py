from tkinter import *

root = Tk()

root.geometry("160x180")
root.title("key")

label = Label(text="keypad")
label.pack(padx=10, pady=10)

e = Entry()
e.pack()

def btn_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def btn_clear():
    e.delete(0, END)

def btn_submit():
    print(e.get())
    e.delete(0, END)

btnframe = Frame()
btnframe.columnconfigure([0,1,2], minsize=40)
btn1 = Button(btnframe, text="1", command=lambda: btn_click(1))
btn2 = Button(btnframe, text="2", command=lambda: btn_click(2))
btn3 = Button(btnframe, text="3", command=lambda: btn_click(3))
btn4 = Button(btnframe, text="4", command=lambda: btn_click(4))
btn5 = Button(btnframe, text="5", command=lambda: btn_click(5))
btn6 = Button(btnframe, text="6", command=lambda: btn_click(6))
btn7 = Button(btnframe, text="7", command=lambda: btn_click(7))
btn8 = Button(btnframe, text="8", command=lambda: btn_click(8))
btn9 = Button(btnframe, text="9", command=lambda: btn_click(9))
btnc = Button(btnframe, text="c", command=btn_clear)
btn0 = Button(btnframe, text="0", command=lambda: btn_click(0))
btns = Button(btnframe, text="send", command=btn_submit)

btn1.grid(row=0, column=0, sticky="nsew")
btn2.grid(row=0, column=1, sticky="nsew")
btn3.grid(row=0, column=2, sticky="nsew")
btn4.grid(row=1, column=0, sticky="nsew")
btn5.grid(row=1, column=1, sticky="nsew")
btn6.grid(row=1, column=2, sticky="nsew")
btn7.grid(row=2, column=0, sticky="nsew")
btn8.grid(row=2, column=1, sticky="nsew")
btn9.grid(row=2, column=2, sticky="nsew")
btnc.grid(row=3, column=0, sticky="nsew")
btn0.grid(row=3, column=1, sticky="nsew")
btns.grid(row=3, column=2, sticky="nsew")
btnframe.pack()

root.mainloop()
