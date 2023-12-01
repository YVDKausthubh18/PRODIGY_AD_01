from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('500x500')

mylabel = Label(root, text='ENTER THE NUMBER', fg='black')
mylabel.grid(row=0, column=0)

enter = Entry(root, borderwidth=10, bg='white')
enter.grid(row=0, column=1)


def number(n):
    current = enter.get()
    enter.delete(0, END)
    enter.insert(0, str(current) + str(n))


def clear():
    enter.delete(0, END)


def equal():
    sec_num = enter.get()
    enter.delete(0, END)
    if math == 'addi':
        enter.insert(0, f_num + int(sec_num))
    if math == 'multiplyc':
        enter.insert(0, f_num * int(sec_num))
    if math == 'subt':
        enter.insert(0, f_num - int(sec_num))
    if math == 'divid':
        enter.insert(0, f_num / int(sec_num))
    if math == 'remin':
        enter.insert(0, f_num % int(sec_num))


def add():
    first_num = enter.get()
    global f_num
    global math
    math = 'addi'
    f_num = int(first_num)
    enter.delete(0, END)


def multiply():
    first_num = enter.get()
    global f_num
    global math
    math = 'multiplyc'
    f_num = int(first_num)
    enter.delete(0, END)


def sub():
    first_num = enter.get()
    global f_num
    global math
    math = 'subt'
    f_num = int(first_num)
    enter.delete(0, END)


def divide():
    first_num = enter.get()
    global f_num
    global math
    math = 'divid'
    f_num = int(first_num)
    enter.delete(0, END)


def rem():
    first_num = enter.get()
    global f_num
    global math
    math = 'remin'
    f_num = int(first_num)
    enter.delete(0, END)


button1 = Button(root, text='1', padx=80, pady=25, command=lambda: number(1), fg='white', bg='grey')
button2 = Button(root, text='2', padx=80, pady=25, command=lambda: number(2), fg='white', bg='grey')
button3 = Button(root, text='3', padx=80, pady=25, command=lambda: number(3), fg='white', bg='grey')
button4 = Button(root, text='4', padx=80, pady=25, command=lambda: number(4), fg='white', bg='grey')
button5 = Button(root, text='5', padx=80, pady=25, command=lambda: number(5), fg='white', bg='grey')
button6 = Button(root, text='6', padx=80, pady=25, command=lambda: number(6), fg='white', bg='grey')
button7 = Button(root, text='7', padx=80, pady=25, command=lambda: number(7), fg='white', bg='grey')
button8 = Button(root, text='8', padx=80, pady=25, command=lambda: number(8), fg='white', bg='grey')
button9 = Button(root, text='9', padx=80, pady=25, command=lambda: number(9), fg='white', bg='grey')
button0 = Button(root, text='0', padx=80, pady=25, command=lambda: number(0), fg='white', bg='grey')
button_add = Button(root, text='+', padx=80, pady=25, command=add, bg='grey', fg='white')
button_equal = Button(root, text='=', padx=80, pady=25, command=equal, bg='sky blue', fg='white')
button_clear = Button(root, text='CE', padx=80, pady=25, command=clear, bg='grey', fg='white')
button_multiply = Button(root, text='x', padx=80, pady=25, command=multiply, bg='grey', fg='white')
button_divide = Button(root, text='/', padx=80, pady=25, command=divide, bg='grey', fg='white')
button_sub = Button(root, text='-', padx=80, pady=25, command=sub, bg='grey', fg='white')
button_rem = Button(root, text='%', padx=80, pady=25, command=rem, bg='grey', fg='white')

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_clear.grid(row=6, column=2 , columnspan=1)
button_equal.grid(row=6, column=1, columnspan=1)
button_add.grid(row=4, column=1)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_sub.grid(row=4, column=2)
button_rem.grid(row=5, column=2)


def exite():
    root.destroy()


button_exit = Button(root, text='Exit Program', command=exite, bg='grey', fg='white')
button_exit.grid(row=7, column=0, columnspan=2)

root.mainloop()
