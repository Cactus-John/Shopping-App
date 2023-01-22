from tkinter import *

master = Tk()
master.geometry("500x500")
master.resizable(False, False)

label = Label(master, text="Home page")
label.pack(side=TOP, pady=10)


def openShop():
    import linking


def openStoreWindow():
    newStoreWindow = Toplevel(master)
    newStoreWindow.title("Store")
    newStoreWindow.geometry("1500x600")
    newStoreWindow.resizable(False, False)
    newStoreWindow_exit_button = Button(newStoreWindow, text="Close",
                                        command=newStoreWindow.destroy,
                                        fg="red",
                                        bg="#E9CE2C",
                                        activeforeground="red",
                                        activebackground="#E9CE2C",
                                        state="active")
    newStoreWindow_exit_button.pack(side=BOTTOM)
    Label(newStoreWindow, text="This is your store! Here are your items and products").pack()


shop_button = Button(master, text="SHOP",
                     command=openShop,
                     fg="#00FF00",
                     bg="black",
                     activeforeground="#00FF00",
                     activebackground="black",
                     state="active")
shop_button.pack(pady=15)

btn = Button(master, text="STORE",
             command=openStoreWindow,
             width=6,
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
