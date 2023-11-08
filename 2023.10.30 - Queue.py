# instructions: declare a queue with 5 elements size, add inte gers 15 and 45, then remove both
# try to remove a third integer, and add 1,2,3,4,5 then try to add 7  to queue

emptyString = " "
queueArray = [emptyString for i in range (5)]
queueSize = len(queueArray)
frontPointer = 0
rearPointer = -1
currentAmount = 0

# personal note
# qS refers to the maximum amount elements that can be stored in the queue.
# we are creating a circular queue. therefore, instead of pushing every elements to the front end after every operation,
# we instead use pointers that will loop back to the front. thus we need to introduce these pointers.
# rP and fP is circular pointers. once it has reached the end of a queue, instead of incrementing, it will be assigned
# to the position of the very front of the queue, which is position 0.
# cA is used to count how many elements are in the queue.
# we use condition rP < qS -1, the reason we have that minus 1, is because although the length of array is 5, the index
# starts from 0 and ends at 4. hence why startPos is 0, endPos is 5-1

print("here's an empty queue")
print(queueArray)

def enqueue(newItem):
    global rearPointer, currentAmount
    if currentAmount < queueSize: # queue is full or not
        if rearPointer < queueSize - 1 : # rP have reached end of queue or not
            rearPointer = rearPointer + 1 # if rP not yet reached end, increment like normal
        else:
            rearPointer = 0 # if rP have reached end, it loops back to front (circular queue)
        currentAmount = currentAmount + 1
        queueArray[rearPointer] = newItem
        print("here's the queue after enqueue")
        print(queueArray)
    else:
        print("Sorry bud the queue is full")


def dequeue():
    global frontPointer, currentAmount
    if currentAmount == 0: # if the queue is empty or not
        print("Sorry bud there's nothing to be dequeued")
    else:
        queueArray[frontPointer] = emptyString # emptying the spot
        if frontPointer == queueSize - 1: #if fP is at the end of the queue, loop back circular to front
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1 # if not yet reached end, increment like normal
        print("here's the queue after dequeue")
        print(queueArray)
        currentAmount = currentAmount - 1

enqueue(15)
enqueue(45)
dequeue()
dequeue()
dequeue()

# personal note
# in range (1,6) will yield values 1,2,3,4,5.
# we dont put in range(5) cuz it will yield 0 until 4.
# we also dont put in range(6) cuz it will yield 0 until 5

for x in range (1,6):
    enqueue(x)

enqueue(7)