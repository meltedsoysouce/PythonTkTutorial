from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My First App')

frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='Your name')

t = StringVar()

entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print(f'Hello, {t.get()}'))

frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

root.mainloop()