myList = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]

lBound = 1
uBound = len(myList)1
index = lBound
foundFlag = False
searchValue = int(input("Please enter an integer: "))

while (foundFlag == False) and (lBound <= uBound):
    index = int((lBound+uBound)/2)
    if myList[index] == searchValue:
        foundFlag = True
        foundIndex = index
    elif myList[index] < searchValue:
        lBound = index + 1
    else:
        uBound = index - 1

if foundFlag == True:
    print("The value is found at", foundIndex)
else:
    print("the value is not found")

