class employee:
    def __init__(self, name, staffno,):
        self.__name = name
        self.__staffno = staffno
        self.__fullTimeStaff = True
    def showDetails(self):
        print("Employee name is", self.__name)
        print("Their staff number is", self.__staffno)

class partTime(employee):
    def __init__(self, name, staffno):
        employee.__init__(self, name, staffno)
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

