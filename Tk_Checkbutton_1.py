from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Checkbutton 1')

frame1 = ttk.Frame(root, padding=(10))
frame1.grid()

v1 = StringVar()
v1.set('0')
cb1 = ttk.Checkbutton(
    frame1, padding=(10), text='Option 1',
    variable=v1,
    command=lambda: print(f'v1 = {v1.get()}'))

v2 = StringVar()
cb2 = ttk.Checkbutton(
    frame1, padding=(10), text='Option 2',
    onvalue='A', offvalue='B',
    variable=v2,
    command=lambda: print(f'v2 = {v2.get()}'))

button1 = ttk.Button(
    frame1, text='show values',
    command=lambda: print(f'v1 = {v1}, v2 = {v2}'))

cb1.grid(row=0, column=0)
cb2.grid(row=0, column=1)
button1.grid(row=1, column=0, columnspan=2)

root.mainloop()