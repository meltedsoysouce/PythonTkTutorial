from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Label Example')

frame1 = ttk.Frame(root)
frame1.grid()

image_sample = PhotoImage(file='./Images/sagyouin_seishi_koujou.png')

label1 = ttk.Label(
    frame1,
    image=image_sample)
label1.grid(row=0, column=0)

label2 = ttk.Label(
    frame1,
    text='Will schools be opwn this filw?',
    padding=(20))
label2.grid(row=0, column=1)

root.mainloop()