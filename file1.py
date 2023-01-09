from tkinter import *
top = Tk()
top.geometry("500x500")
top.title("My first GUI App")

label1 = Label(top,text="Admission Form").place(x=150,y=50)

label2 = Label(top,text="Enter Your Name").place(x=100,y=100)
entry1 = Entry(top).place(x=100,y=150)

label3 = Label(top,text="Enter Your Mobile").place(x=100,y=200)
entry2 = Entry(top).place(x=100,y=250)

button1 = Button(top,text="submit").place(x=120,y=300)
button2 = Button(top,text="cancel").place(x=200,y=300)
top.mainloop()
