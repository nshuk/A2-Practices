class studentRecord:
    def __init__(self,n,a,c):
        self.__name = n
        self.__address = a
        self.__class = c
    def getName(self):
        return(self.__name)
    def getAddress(self):
        return(self.__address)
    def getClass(self):
        return(self.__class)


student1 = studentRecord("Naqib", "Selangor", "PointFour")
student2 = studentRecord("Hazni", "Selangor", "PointTwo")
student3 = studentRecord("Aimi", "Selangor", "PointEight")
newline = "\n"

# write data

def writeData(record, location):
    global newline
    studentFile = open(location, "w")
    studentFile.write(record.getName())
    studentFile.write(newline)
    studentFile.write(record.getAddress())
    studentFile.write(newline)
    studentFile.write(record.getClass())
    studentFile.write(newline)
    studentFile.close()

writeData(student1, "C:/9618/Feb6(1).txt")

# append data

def appendData(record, location):
    global newline
    studentFile = open(location, "a")
    studentFile.write(newline)
    studentFile.write(record.getName())
    studentFile.write(newline)
    studentFile.write(record.getAddress())
    studentFile.write(newline)
    studentFile.write(record.getClass())
    studentFile.close()

appendData(student2, "C:/9618/Feb6(1).txt")

# read data

def readData(location):
    studentFile = open(location, "r")
    text = studentFile.readline()
    while len(text)>0:
        print(text)
        text = studentFile.readline()
    studentFile.close()

readData("C:/9618/Feb6(1).txt")

# input data

print("Please enter the following data:")
n = input("Name: ")
a = input("Address: ")
c = input("Class: ")

student4 = studentRecord(n,a,c)
writeData(student4, "C:/9618/Feb6(2).txt")
readData("C:/9618/Feb6(2).txt")


