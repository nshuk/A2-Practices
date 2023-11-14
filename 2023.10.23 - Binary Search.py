myList = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]

lBound = 0
uBound = len(myList)
index = lBound
foundFlag = False
searchValue = int(input("Please enter an integer: "))

while (foundFlag == False) and (lBound <= uBound):
    index = int((lBound+uBound)/2) # ensure the use of int because index are whole numbers only
    if myList[index] == searchValue:
        foundFlag = True
        foundIndex = index
    elif myList[index] < searchValue: # if item in middle array < the search item
        lBound = index + 1 # go right. meaning lbound is shifted to the right
    else:
        uBound = index - 1 # go left. meaning ubound is shifted to the left

if foundFlag == True:
    print("The value is found at", foundIndex)
else:
    print("the value is not found")

# our index starts with 0, all the way until index 9
# since we have 10 items in our array, the len mylist will also bring about the value 9 cuz it starts counting from 0
# arrays of bsearch has to be pre-arranged in ascending order first 
# binary search will start from the middle of array, then go left or right depending on the value of the search item
# 
