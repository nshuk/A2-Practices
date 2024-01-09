def AreaSquare():
    length = float(input("Length: "))
    area = length * length
    print("Area is: ", area)

def AreaRectangle():
    length = float(input("Length: "))
    height = float(input("Height: "))
    area = length * height
    print("Area is: ", area)

def AreaTriangle():
    width = float(input("Width: "))
    height = float(input("Height: "))
    area = width * height * 0.5
    print("Area is: ", area)

def AreaParallelogram():
    length1 = float(input("Length of one side: "))
    length2 = float(input("Length of the other side: "))
    height = float(input("Height: "))
    area = (length1+length2) * height * 0.5
    print("Area is: ", area)

def AreaCircle():
    radius = float(input("Radius: "))
    area = 3.142 * radius * radius
    print("Area is: ", area)

print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Parallelogram")
print("5. Circle")
choice = int(input("Enter choice of area: "))

if choice>5 or choice<1:
    print("Invalid Choice")
elif choice == 1:
    AreaSquare()
elif choice == 2:
    AreaRectangle()
elif choice == 3:
    AreaTriangle()
elif choice == 4:
    AreaParallelogram()
elif choice == 5:
    AreaCircle()
