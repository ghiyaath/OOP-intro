from tkinter import *

from tkinter import messagebox

root = Tk()
root.geometry("1000x700")
root.config(bg="light blue")
root.resizable(False, False)
root.title("Area of a circle")


# Defining The Function
def calculate():
    try:
        radius = float(e1.get())
        answer = 3.14*radius*radius
        e2.config(state="normal")
        e2.delete(0, END)
        e2.insert(0, answer)
        e2.config(state="readonly")
    except ValueError as ex:
        e1.config(state="normal")
        e1.delete(0, END)
        e1.config(state="readonly")

        e2.config(state="normal")
        e2.delete(0, END)
        e2.config(state="readonly")


def button_Exit():
    msg_box = messagebox.askquestion("Terminating program", "Are you sure you want to close this program? ", icon="Warning")
    if msg_box == "yes":
        root.destroy()


# Labels
l1 = Label(root, text="Enter the radius of a circle:", bg="gray")
l1.place(x=50, y=200)
l2 = Label(root, text="Area of the circle is:", bg="gray")
l2.place(x=50, y=300)


# Entries
e1 = Entry(root, width=20)
e1.place(x=250, y=200)
e2 = Entry(root, width=20, state="readonly")
e2.place(x=250, y=300)


# Buttons
b1 = Button(root, text="Calculate the area", command=calculate, bg="yellow", fg="black")
b1.place(x=150, y=400)
b2 = Button(root, text="Exit", command=button_Exit, bg="yellow", fg="black")
b2.place(x=450, y=400)

# Run program
mainloop()
