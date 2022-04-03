from tkinter import *
from tkinter import ttk

def dvd_clicked():
    button1.state(['pressed'])
    button2.state(['!pressed'])
    s.set('DVD Clicked.')

def download_clicked():
    button1.state(['!pressed'])
    button2.state(['pressed'])
    s.set("Download clicked.")

root = Tk()
root.title('Button Example')

frame1 = ttk.Frame(
    root,
    padding=(5))
frame1.grid()

icon1 = PhotoImage(file='./Image/sample.png')
button1 = ttk.Button(
    frame1,
    image=icon1,
    text='DVD',
    compound=TOP,
    padding=(10),
    command=dvd_clicked)
button1.grid(row=0, column=0)

icon2 = PhotoImage(file='./Image/Sample2.png')
button2 = ttk.Button(
    frame1,
    image=icon2,
    text='Download',
    compound=TOP,
    command=TOP,
    padding=(10),
    command=download_clicked)

s = StringVar()
label1 = ttk.Label(
    frame1,
    textvariable=s)
label1.grid(row=1, column=0, columnspan=2)

root.mainloop()