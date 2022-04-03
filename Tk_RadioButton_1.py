from cProfile import label
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Raddiobutton 1')

frame1 = ttk.Frame(root, padding=10)

ttk.Style().theme_use('classic')

label_frame = ttk.LabelFrame(
    frame1,
    text='Options',
    padding=(10),
    style='My.TLabelframe')

v1 = StringVar()
rb1 = ttk.Radiobutton(
    label_frame,
    text='Option A',
    value='A',
    variable=v1)

rb2 = ttk.Radiobutton(
    label_frame,
    text='Option B',
    value='B',
    variable=v1)

button1 = ttk.Button(
    frame1,
    text='OK',
    padding=(20, 5),
    command=lambda: print(f'va={v1.get()}'))

frame1.grid()
label_frame.grid(row=0, column=0)
rb1.grid(row=0, column=0)
rb2.grid(row=0, column=1)
button1.grid(row=1, pady=5)

root.mainloop()