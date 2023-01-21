from tkinter import *

def click():
    print("You clicked the button")


window = Tk()
photo = PhotoImage(file="W:\Projects\Ivan\VS\pythonApp\dawnFM.png")

button = Button(window, text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state="active",
                image=photo,
                compound="top")

button.pack()

window.mainloop()

