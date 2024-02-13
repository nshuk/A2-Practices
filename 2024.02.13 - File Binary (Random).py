class petRecord:
    def __init__(self, n, s, id):
        self.name = n
        self.species = s
        self.ID = id
    def getName(self):
        return self.name
    def getSpecies(self):
        return self.species
    def getID(self):
        return self.ID

import pickle
pet1 = petRecord("Pin Pon", "Cat", 12)
newline = "\n"

def writeData(record, location):
    file = open(location, "w+b")
    address = hash(record.ID)
    file.seek(address)
    pickle.dump(record, file)
    file.close()

def retrieveData(location):
    global newline
    file = open(location, "rb")
    ID = int(input("\nEnter pet ID to retrieve data: "))
    try:
        address = hash(ID)
        file.seek(address)
        record = pickle.load(file)
        print(newline, "Name:", record.name, newline, "Species:", record.species)
    except:
        print("Error ID does not exist")
    file.close()

writeData(pet1, "C:/9618/Feb13(2).DAT")
retrieveData("C:/9618/Feb13(2).DAT")