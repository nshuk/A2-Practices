class shape:
    def __init__(self):
        self.__areaValue = 0
    def area(self):
        print("The area is:", self.__areaValue)

class rectangle(shape):
    def __init__(self, l , w):
        shape.__init__(self)
        self.__length = l
        self.__width = w
    def area(self):
        self.__areaValue = (self.__length) * (self.__width)
        print("The rectangle area is:", self.__areaValue)

class circle(shape):
    def __init__(self, r):
        shape.__init__(self)
        self.__radius = r
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

myRectangle = rectangle(3, 5)
myCircle = circle(4)
mySquare = square(5)

myRectangle.area()
myCircle.area()
mySquare.area()

# polymorphism is when a method in a superclass (in this case method area) is redefined in the subclass
# the redefined method bears the same name, but with exclusive features to the subclass