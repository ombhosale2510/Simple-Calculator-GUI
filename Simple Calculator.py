from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure(background='black')
root.resizable(False, False)

e = Entry(root, width=45, borderwidth=5)
e.focus()
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)


def button_click(number):
    current = e.get()
    # put e.del so it doesnt print earlier inputs again instead just keeps the inputs
    e.delete(0, END)
    # Put it in str() so it concatenates instead of add
    e.insert(0, str(current) + str(number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_clear():
    e.delete(0, END)


# Defining and placing the buttons (NUMBERS)
button_1 = Button(root, text="1", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(1), activebackground='black', activeforeground='white')
button_1.grid(row=3, column=0)

button_2 = Button(root, text="2", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(2), activebackground='black', activeforeground='white')
button_2.grid(row=3, column=1)

button_3 = Button(root, text="3", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(3), activebackground='black', activeforeground='white')
button_3.grid(row=3, column=2)

button_4 = Button(root, text="4", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(4), activebackground='black', activeforeground='white')
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(5), activebackground='black', activeforeground='white')
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(6), activebackground='black', activeforeground='white')
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(7), activebackground='black', activeforeground='white')
button_7.grid(row=1, column=0)

button_8 = Button(root, text="8", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(8), activebackground='black', activeforeground='white')
button_8.grid(row=1, column=1)

button_9 = Button(root, text="9", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(9), activebackground='black', activeforeground='white')
button_9.grid(row=1, column=2)

button_0 = Button(root, text="0", font="Consolas", padx=40, pady=20, fg='white', bg='black',
                  command=lambda: button_click(0), activebackground='black', activeforeground='white')
button_0.grid(row=4, column=0)

# Defining and placing the buttons (OPERATIONS)
button_add = Button(root, text="+", font="Consolas", fg='orange', bg='black', padx=40, pady=20,
                    command=button_add, activebackground='black', activeforeground='orange')
button_add.grid(row=5, column=0)

button_subtract = Button(root, text="-", font="Consolas", fg='orange', bg='black', padx=40, pady=20,
                         command=button_subtract, activebackground='black', activeforeground='orange')
button_subtract.grid(row=6, column=0)

button_multiply = Button(root, text="*", font="Consolas", fg='orange', bg='black', padx=40, pady=20,
                         command=button_multiply, activebackground='black', activeforeground='orange')
button_multiply.grid(row=6, column=1)

button_divide = Button(root, text="/", font="Consolas", fg='orange', bg='black', padx=40, pady=20,
                       command=button_divide, activebackground='black', activeforeground='orange')
button_divide.grid(row=6, column=2)

button_equals = Button(root, text="=", font="Consolas", fg='orange', bg='black', padx=92, pady=20,
                       command=button_equal, activebackground='black', activeforeground='orange')
button_equals.grid(row=4, column=1, columnspan=2)

button_clear = Button(root, text="CE", font="Consolas", fg='orange', bg='black', padx=87, pady=20,
                      command=button_clear, activebackground='black', activeforeground='orange')
button_clear.grid(row=5, column=1, columnspan=2)

root.mainloop()
