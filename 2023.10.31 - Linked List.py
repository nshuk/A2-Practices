# LL is linked list, P is pointer, F is flag

myLL = [27,19,36,42,16,0,0,0,0,0,0,0]
myLLP = [-1,0,1,2,3,6,7,8,9,10,11,-1]

# here, the LL is filled until index 4. starting from index 5, the LL is empty
# so what's the use of heapstartP? basically it will point to index with an empty slot right next to the filled
# and when you wanna insert a new item, that the item will be added at that heap, and it will become the new startp
nullP = -1
startP = 4
heapStartP = 5

print("Here's the initial LL and its LLP")
print(myLL)
print(myLLP)

def searchLL(searchVal):
    foundF = False # dont use global foundF and ItemP cuz for each finds, then flag has to be reset to false
    itemP = startP
    while (itemP != nullP) and (foundF == False): # while havent reached end node and still havent found
        if myLL[itemP] == searchVal:
            foundF = True
        else:
            itemP = myLLP[itemP] # LL exclusive
    return itemP

itemIndex = searchLL(27)

if itemIndex != nullP:
    print("The value is found at index ", itemIndex)
else:
    print("The value is not found")

def insertLL(newItem): # here, we are inserting the item at the very front
    global heapStartP, startP
    if heapStartP == nullP: # check if ll is full
        print("Linked list is full bro")
    else:
        tempP = startP # keep old startP
        startP = heapStartP # set startP to next position in heap
        heapStartP = myLLP[heapStartP] # reset heap startP
        myLL[startP] = newItem # insert item
        myLLP[startP] = tempP # update LLP
        print("Here's the current LL with its LLP")
        print(myLL)
        print(myLLP)

insertLL(18)