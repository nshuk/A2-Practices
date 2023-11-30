arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch (searchValue):
    foundFlag = False # dont global foundflag cuz we want to reset the flag to false each call
    for x in range(10): # this is the part where it will check from index 0 to index 9
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

