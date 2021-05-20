class Shapes:

    def __init__(self, type, name, size, side):

        self.type = type
        self.name = name
        self.size = size
        self.side = side

    def area(self):

        print("I am a " + self.type + "\n"+
            "Name is "+ self.name + "\n" +
            "size is " + self.size + "\n" +
            "number of sides " + self.side)
#object name can be anything, preferably start with "obj" so you know its an object
#call the class name you're going to use, the methods you wanna use.
#inside the brackets are the values given by a user to input into the able method
objShapes=Shapes("Quadrilateral", "square", "20cm", "5")
#object named will use the method area in the above class called area
objShapes.area()


#Subclass
class Circle(Shapes):
    #Shapes attributes will be inheritted therefore it'll show when this SubClass is called
    #radius is an extra attribute that was not inherited
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        #answer is declared to have the followinfg calculation
        answer = 3.14*int(self.radius)**2
        #same as above print, calls the previously declared calculation
        #must be converted to string bc calculation is in integer
        print("The area of circle is : "+ str(answer))
#object name declared
# is equal to the name of the Subclass Circle
#6 is the "input" from the user
objCircle = Circle(6)
objCircle.area()

class Triangle(Shapes):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        answer = (self.height*self.base)/2
        print("Area of triangle is "+ str(answer))
objTriangle = Triangle(5,8)
objTriangle.area()

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area = self.width*self.length
        print("Area of Rectangle is " + str(area))
objRectangle = Rectangle(10, 7)
objRectangle.area()
class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        area = self.side**2
        print("Area of Square is :" + str(area))
objSquare = Square(5)
objSquare.area()


