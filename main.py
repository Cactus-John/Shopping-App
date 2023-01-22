from tkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


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


def openShopWindow():
    newShopWindow = Toplevel(master)
    newShopWindow.title("Shop")
    newShopWindow.geometry("1500x600")
    newShopWindow.resizable(False, False)
    newShop_exit_button = Button(newShopWindow, text="Close",
                                 command=newShopWindow.destroy,
                                 fg="red",
                                 bg="#E9CE2C",
                                 activeforeground="red",
                                 activebackground="#E9CE2C",
                                 state="active")
    newShop_exit_button.pack(side=BOTTOM)
    Label(newShopWindow, text="Welcome! This is your shopping window").pack()


def goShopping():
    shopping_button = Button(openShopWindow, text="Go shopping",
                            command=openShopWindow,
                            width=10,
                            fg="#00FF00",
                            bg="black",
                            activeforeground="#00FF00",
                            activebackground="black",
                            state="active")
    shopping_button.pack(pady=15)
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.amazon.de/')
    shopping_button = browser.find_element_by_link_text('Best Sellers')
    shopping_button.click()
    time.sleep(3)


master = Tk()
master.geometry("500x500")
master.resizable(False, False)

label = Label(master, text="Home page")
label.pack(side=TOP, pady=10)

shop_button = Button(master, text="SHOP",
                     command=openNewWindow,
                     fg="#00FF00",
                     bg="black",
                     activeforeground="#00FF00",
                     activebackground="black",
                     state="active")
shop_button.pack(pady=15)

btn = Button(master, text="STORE",
             command=openNewWindow,
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
