arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch (searchValue):
    foundFlag = False
    for x in range(10):
        if arrayData[x] == searchValue:
            foundFlag = True

    if foundFlag == True:
        return True
    else:
        return False

searchValue = int(input("Please enter an integer: "))

foundF = linearSearch(searchValue)

if foundF == True:
    print("Found it bro")
else:
    print("Sorry bro")

