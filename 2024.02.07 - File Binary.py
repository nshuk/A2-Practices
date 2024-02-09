# writing, appending, reading to a binary file (.DAT)

class carRecord:
    def __init__(self,b,t,m):
        self.__brand = b
        self.__type = t
        self.__model = m
    def getBrand(self):
        return self.__brand
    def getType(self):
        return self.__type
    def getModel(self):
        return self.__model

car1 = carRecord("Chevrolet", "Muscle Car", "Camaro SS")
car2 = carRecord("Tesla", "EV", "Model S" )
newline = "\n"

# use of pickle library to w,a,r binary file
# the format for pickle dump is pickle.dump(data, file)
# the format for pickle load is pickle.load(file)
# use of w+b, ab, and rb instead of w, a, and r

import pickle

# writing a data

def writeData(record, location):
    global newline
    carFile = open(location, "w+b")  # create a new DAT and write the data
    pickle.dump(record.getBrand(), carFile)
    pickle.dump(record.getType(), carFile)
    pickle.dump(record.getModel(), carFile)
    pickle.dump(newline, carFile)
    carFile.close()

# if file of the same name already exists, it will overwrite existing file
# works similarly as txt file

writeData(car1, "C:/9618/Feb7(1).DAT")

# appending a data

def appendData(record, location):
    global newline
    carFile = open(location, "ab")  # create a new DAT and write the data
    pickle.dump(record.getBrand(), carFile)
    pickle.dump(record.getType(), carFile)
    pickle.dump(record.getModel(), carFile)
    pickle.dump(newline, carFile)
    carFile.close()

appendData(car2, "C:/9618/Feb7(1).DAT")

# reading a data

def readData(location):
    carFile = open(location, "rb")
    array = []
    while True:
        try:
            carData=pickle.load(carFile)
        except EOFError:
            break
        array.append(carData)
    for i in range(len(array)):
        print(array[i])
    carFile.close()

readData("C:/9618/Feb7(1).DAT")
