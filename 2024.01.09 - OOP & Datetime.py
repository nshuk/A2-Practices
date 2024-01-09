class employee:
    def __init__(self, name, staffno, department):
        self.name = name
        self.staffno = staffno
        self.department = department
    def showDetails(self):
        print("Employee name is " + self.name)
        print("Their staff number is " + self.staffno)
        print("Their department is " + self.department)

myStaff = employee("Naqib", "ALE22122" , "Engineering")
myStaff.showDetails()

print(" ")

class student:
    def __init__(self, name, dateOfBirth, examMark):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__examMark = examMark
    def displayExamMark(self):
        print("The exam mark for", self.__name, "is" , self.__examMark)

# taking inputs from the user
name = input("Please enter student name: ")
print("Enter their date of birth")
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
import datetime # use of datetime library to use the date format
dateOfBirth = datetime.date(year, month, day) # use datetime.date
examMark = input("Please enter their exam marks: ")

# using the inputs on the object
myStudent = student(name, dateOfBirth, examMark)
myStudent.displayExamMark()