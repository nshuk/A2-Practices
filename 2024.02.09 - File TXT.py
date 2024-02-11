DataArray = [0 for i in range(80)]
# declare array[0:79] of integer

def readFile(location):
    file = open(location, "r")
    text = file.readline()
    i = 0
    while len(text)>0:
        DataArray[i] = int(text)
        text = file.readline()
        i = i + 1
    file.close()


def readFile2(location): # another way of reading  using exception handling
    try:
        file = open(location, "r")
        for i in range(80):
            text = file.readline()
            DataArray[i] = int(text)
        file.close()
    except IOError:
        print("File doesn't exist")

def FindValues():
    searchValue = int(input("Enter search value: "))
    if (searchValue < 0) or (searchValue > 80):
        print("Invalid Number")
        return FindValues()
    count = 0
    for x in range(80):  # it will check from index 0 to index 79
        if DataArray[x] == searchValue:
            count = count + 1
    return count



readFile("C:/9618/Feb9/Integer.txt")
numAppeared = FindValues()
print("The amount of the integer appeared is", numAppeared)

def BubbleSort():
    global DataArray
    lbound = 0
    uBound = len(DataArray) - 1
    n = uBound
    swapFlag = False

    print("The unsorted array is: ", DataArray)
    while (swapFlag == False) or (n > 0):
        for i in range(lbound, n):  # start lbound, end at n-1
            if DataArray[i] > DataArray[i + 1]:  # if greater
                temp = DataArray[i]  # swapping values
                DataArray[i] = DataArray[i + 1]
                DataArray[i + 1] = temp
                swapFlag = True  # raise the flag
        n = n - 1

    print("After ascending sorting, the array is: ", DataArray)

BubbleSort()