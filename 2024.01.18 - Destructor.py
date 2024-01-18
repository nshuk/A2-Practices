class shape:
    def __init__(self):
        self.__areaValue = 0
    def area(self):
        print("The area is:", self.__areaValue)
class circle(shape):
    def __init__(self, r):
        shape.__init__(self)
        self.__radius = r
    def __del__(self):  # delete instance right after program ends
        print("Circle shape deleted")
    def area(self):
        self.__areaValue = 3.142 * (self.__radius) * (self.__radius)
        print("The circle area is:", self.__areaValue)

class square(shape):
    def __init__(self, l):
        shape.__init__(self)
        self.__length = l
    def area(self):
        self.__areaValue = (self.__length) * (self.__length)
        print("The square area is:", self.__areaValue)


myCircle = circle(4) # will automatically delete itself when the program ends
myCircle.area()

mySquare = square(5)
mySquare.area()
del mySquare # manually delete instance.



# destructor is a method that is invoked to destroy an object

# use of def__del__(self) within the class definition
# if you were to run this program, the final output would be "circle shape deleted"
# this means that the program will run whatever it is doing until it the program ends
# right before the program ends, it will then self delete the instantation myCircle

# use of del object on the main program to manually delete an object immediately
# if you were to use method are on mySquare after this, error occurs cux it doesn't exist