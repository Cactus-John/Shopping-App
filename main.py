from tkinter import *


def click():
    print("You clicked the button")


def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("Store")
    newWindow.geometry("1500x600")
    newWindow.resizable(False, False)
    newWindow_exit_button = Button(newWindow, text="Close",
                                   command=newWindow.destroy,
                                   fg="red",
                                   bg="#E9CE2C",
                                   activeforeground="red",
                                   activebackground="#E9CE2C",
                                   state="active")
    newWindow_exit_button.pack(side=BOTTOM)
    Label(newWindow, text="This is your store! Here are your items and products").pack()


master = Tk()
master.geometry("500x200")
master.resizable(False, False)

label = Label(master, text="Home page")
label.pack(side=TOP, pady=10)

btn = Button(master, text="Click to open your store of items and products",
             command=openNewWindow,
             fg="#00FF00",
             bg="black",
             activeforeground="#00FF00",
             activebackground="black",
             state="active")
btn.pack(pady=10)

exit_button = Button(master, text="Close",
                     command=master.destroy,
                     fg="red",
                     bg="#E9CE2C",
                     activeforeground="red",
                     activebackground="#E9CE2C")
exit_button.pack(side=BOTTOM, pady=10)


mainloop()
