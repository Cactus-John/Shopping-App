from tkinter import *
import webbrowser

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


def delete():
    link_entry.delete(1)


def close():
    root.destroy()


def accept():
    import amazon_cart


root = Tk()
root.geometry('420x360')
root.title("URL parser")
root.resizable(False, False)
link_entry = Entry(root, width=50)
link_entry.pack(pady=5)
link_button = Button(root, text="Accept",
                     command=accept,
                     fg="red",
                     bg="#E9CE2C",
                     activeforeground="red",
                     activebackground="#E9CE2C",
                     state="active")
link_button.place(x=120, y=35)

link_delete = Button(root, text="Delete",
                     command=delete,
                     fg="red",
                     bg="#E9CE2C",
                     activeforeground="red",
                     activebackground="#E9CE2C",
                     state="active")
link_delete.place(x=240, y=35)

link_destroy = Button(root, text="Close",
                      command=close,
                      fg="red",
                      bg="#E9CE2C",
                      activeforeground="red",
                      activebackground="#E9CE2C",
                      state="active")
link_destroy.pack(side=BOTTOM)


mainloop()
