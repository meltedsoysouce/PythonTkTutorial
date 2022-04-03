from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

frame1 = ttk.Frame(
    root,
    padding=10)
frame1.grid()

icon = PhotoImage(file='./Images/sample.png')

label1 = ttk.Label(
    frame1,
    image=icon)
label1.grid(row=0, column=0)

label2 = ttk.Label(
    frame1,
    text='Will schools be open this fall?',
    width=20,
    anchor=W,
    padding=(20))

button1 = ttk.Button(
    frame1,
    text='Ok',
    command=lambda: root.quit())
button1.grid(row=1, column=0, columnspan=2)

root.mainloop()