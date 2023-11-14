myList = [53,21,60,18,42,19]

print("The unsorted array is: ", myList)

upBound = len(myList)
lowBound = 0

for x in range ((lowBound +1), upBound): #start at lbound-1, end at upbound -1
    left = x - 1 
    current = myList[x]
    if myList[left] > current:
        while (myList[left] > current) and (left >-1):
            temp = myList[left+1]
            myList[left+1] = myList[left]
            myList[left] = temp
            left = left - 1 # go the previous element at the back, until left = -1 (reaches beginnig of list)

print ("The sorted array is: ", myList)

# the way isort is implemented:
# the outer loop (for x in range) iterates over each element in the list, starting from the second element (x = 1)
# left = x - 1 initializes the variable left to the index one position before the current element
# current = myList[x] stores the value of the current element
# the if statement checks if the element to the left of the current element is greater than the current element. if true, it enters the nested while loop, 
# and if it isnt true, meaning already sorted, therefore we'll go to the next value of x
# the while loop swaps elements to the right until the correct position for the current element is found within the sorted portion of the list
# it continues swapping until the left element is no longer greater than the current element or until it reaches the beginning of the list (left > -1).
