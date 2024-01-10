class Car:
    def __init__(self,n,e):
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration =  None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    def SetPurchasePrice(self,p):
        self.__PurchasePrice = p
    def SetRegistration(self, r):
        self.__Registration = r
    def GetVehicleID(self):
        return(self.__VehicleID)
    def GetRegistration(self):
        return(self.__Registration)
    def GetDateOfRegistration(self):
        return(self.__DateOfRegistration)
    def GetEngineSize(self):
        return(self.__EngineSize)
    def GetPurchasePrice(self):
        return(self.__PurchasePrice)

#Instantiating a class
ThisCar = Car("ABC1234", 2500)

#Using a method
ThisCar.SetPurchasePrice(12000)

print(ThisCar.GetPurchasePrice())
print(ThisCar.GetVehicleID())


# second example
# companyname and email in constructor, datelastcontact in setter

import datetime # use of datetime library to use the date format
class Company:
    def __init__(self, n, e): #constructor
        self.__companyName = n
        self.__emailAddress = e
        self.__dateLastContact = None #absence of value

    def SetDateLastContact(self): #setter
        print("Enter date of last contact below")
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        self.__dateLastContact = datetime.date(year, month, day)
    def GetCompanyName(self):
        return(self.__companyName)
    def GetEmailAddress(self):
        return(self.__emailAddress)
    def GetDateLastContact(self):
        return(self.__dateLastContact)


myCompany = Company("MARA", "naqib@gmail.com")

myCompany.SetDateLastContact()

print(myCompany.GetCompanyName())
print(myCompany.GetEmailAddress())
print(myCompany.GetDateLastContact())
