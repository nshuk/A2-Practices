class employee:
    def __init__(self, name, staffno,):
        self.__name = name
        self.__staffno = staffno
        self.__fullTimeStaff = True
    def showDetails(self):
        print("Employee name is", self.__name)
        print("Their staff number is", self.__staffno)

class partTime(employee): # inherited class must have its superclass as parameter otherwise you cant call the superclass. self will be higlighted
    def __init__(self, name, staffno): # ensure the parameters of superclass is present, only then add the subclass-specific parameters
        employee.__init__(self, name, staffno) # this is how you inherit from a superclass. ensure the parameters are identical
        self.__fullTimeStaff = False
        self.__hoursWorked = 0
    def getHoursWorked(self):
        return self.__hoursWorked

class fullTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
        self.__fullTimeStaff = True
        self.__yearlySalary = 0
    def getYearlySalary(self):
        return self.__yearlySalary

permanentStaff = fullTime("Eric Jones", 72)
permanentStaff.showDetails()
temporaryStaff = partTime("Alice Hue", 1017)
temporaryStaff.showDetails()

# second example

class student:
    def __init__(self, name, DOB, mark):
        self.__name = name
        self.__dateOfBirth = DOB
        self.__examMark = mark
        self.__fullTimeStudent = True
    def displayExamMark(self):
        return self.__examMark

class partTimeStudent(student):
    def __init__(self, name, DOB, mark):
        student.__init__(self, name, DOB, mark)
        self.__fullTimeStudent = False

class fullTimeStudent(student):
    def __init__(self, name, DOB, mark):
        student.__init__(self, name, DOB, mark)
        self.__fullTimeStudent = True


import datetime
permanentStudent = fullTimeStudent("Naqib", datetime.date(2004,7,10), 85)
print("Mark is:", permanentStudent.displayExamMark())
temporaryStudent = fullTimeStudent("Amin", datetime.date(2004,12,10), 90)
print("Mark is:", temporaryStudent.displayExamMark())

# winter 17 variant 3 question 6

class Account:
    def __init__(self):
        self.__accountNumber = None #string
        self.__balance = None #currency
    def SetAccountNumber(self, n):
        self.__accountNumber = n
    def SetBalance(self, n):
        self.__balance = n
    def GetAccountNumber(self):
        return self.__accountNumber
    def GetBalance(self):
        return self.__balance

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
        self.__regularPayment = None #real
        self.__paymentInterval = None #integer

# winter 2015 variant 2 question 3
# all properties are in constructor for both super and subclass
# look at how the superclass constr are written within subclass constr

class Student:
    def __init__(self, n, DOB):
        self.__studentName = n #string
        self.__DOB = DOB #date
    def ShowStudentName(self):
        return self.__studentName
    def ShowDOB(self):
        return self.__DOB

class FullTimeStudent(Student):
    def __init__(self, n, DOB, a, t):
        Student.__init__(self, n, DOB) # superclass' constr does not include the new properties
        self.__address = a #string
        self.__telephoneNumber = t #string
    def ShowAddress(self):
        return self.__address
    def ShowTelephoneNumber(self):
        return self.__telephoneNumber

import datetime
NewStudent = FullTimeStudent("A. Nyone", datetime.date(1990,11,12), "Selangor", "099111")
print(NewStudent.ShowStudentName())
print(NewStudent.ShowDOB())
print(NewStudent.ShowAddress())
print(NewStudent.ShowTelephoneNumber())

# winter 2015 variant 1 question 3

class StockItem:
    def __init__(self, n, d, l):
        self.__title = n #string
        self.__date = d # date
        self.__loan = l # boolean
    def ShowTitle(self):
        return self.__title
    def ShowDate(self):
        return self.__date
    def ShowLoan(self):
        return self.__loan

class Book(StockItem):
    def __init__(self, n, d, l, a, i):
        StockItem.__init__(self, n, d, l)
        self.__author = a #string
        self.__ISBN = i #string
    def ShowAuthor(self):
        return self.__author
    def ShowISBN(self):
        return self.__ISBN

import datetime
NewBook = Book("Computers", datetime.date(2001,11,12), False, "A.Nyone", "099111")
print(NewBook.ShowTitle())
print(NewBook.ShowDate())
print(NewBook.ShowLoan())
print(NewBook.ShowAuthor())
print(NewBook.ShowISBN())

# inheritance1 file question 4

class Member:
    def __init__(self, n, id, s):
        self.__memberName = n #string
        self.__memberID = id #integer
        self.__subscriptionPaid = s #boolean
    def GetMemberName(self):
        return self.__memberName
    def GetMemberID(self):
        return self.__memberID
    def GetSubscriptionPaid(self):
        return self.__subscriptionPaid

class JuniorMember(Member):
    def __init__(self, n, id, s, DOB):
        Member.__init__(self, n, id, s)
        self.__dateOfBirth = DOB #date
    def GetDateOfBirth(self):
        return self.__dateOfBirth

NewMember = JuniorMember("Ahmed", 12347, True, datetime.date(2001,11,12))
print(NewMember.GetMemberName())
print(NewMember.GetMemberID())
print(NewMember.GetSubscriptionPaid())
print(NewMember.GetDateOfBirth())
