from tkinter import *


window = Tk()
window.title("My First GUI Tkinter Program")
window.minsize(width=500, height=300)

def button_clicked():
    my_label.config(text=input.get())
    my_label.pack()

#label
my_label = Label(text="Hello, Sai!", font=("Calibri", 24, "normal"))
my_label.pack()

#Button
mybutoon = Button(text="Click Me", command=button_clicked)
mybutoon.pack()

#Entry
input = Entry(width= 10)
input.pack()




window.mainloop()