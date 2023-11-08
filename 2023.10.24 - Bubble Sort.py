myList = [27,19,36,42,16,89,21,16,55]

lbound = 0
uBound = 9
n = uBound - 1
swapFlag = False

print("The unsorted array is: ", myList)
while (swapFlag == False) or (n>0):
    for i in range(lbound,n):
        if myList[i] > myList[i+1]:
            temp = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = temp
            swapFlag = True
    n = n - 1

print("After ascending sorting, the array is: ", myList)

#Reinitialize the changing variables
swapFlag = False
n = uBound -1

while (swapFlag == False) or (n>0):
    for i in range(lbound,n):
        if myList[i] < myList[i+1]:
            temp = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = temp
            swapFlag = True
    n = n - 1

print("After descending sorting, the array is: ", myList)