myList = [53,21,60,18,42,19]

print("The unsorted array is: ", myList)

upBound = len(myList)
lowBound = 0

for x in range ((lowBound +1), upBound):
    left = x - 1
    current = myList[x]
    if myList[left] > current:
        while (myList[left] > current) and (left >-1):
            temp = myList[left+1]
            myList[left+1] = myList[left]
            myList[left] = temp
            left = left - 1

print ("The sorted array is: ", myList)