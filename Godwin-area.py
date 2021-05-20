from tkinter import *
root=Tk()
root.title("OOP using tkinter")
root.geometry("300x300")
class Circle:
    myresult=StringVar()
    def __init__(self, window):
        self.lblradius=Label(window, text="Please enter the radius")
        self.lblradius.pack()
        self.txtrad=Entry(window)
        self.txtrad.pack()
        self.btncalc=Button(window, text="Calculate area", borderwidth="10", command=self.area)
        self.btncalc.pack()
        self.lblresult=Label(window, text="", textvariable=self.myresult)
        self.lblresult.pack()

    def area(self):
        radius = int(self.txtrad.get())
        answer = 3.14*(radius**2)
        self.myresult.set("The area is " + str( answer))
obj_circle=Circle(root)

root.mainloop()
