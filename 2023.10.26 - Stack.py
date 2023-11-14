emptyString = " "
stackArray = [emptyString for i in range (10)]

nullPointer = -1
topPointer = -1
stackSize = len(stackArray)

# basically topPointer will start at position -1, then will increase or decrease based on the amount of current elements
# null pointer is a constant which tells us whether we have reached the empty stack or not
# global is used when you update a value of variable in a procedure, and you want it to also update in the main program
# to know which variable should be globaled, try to write the code with the variables first, if turns into the colour
# grey instead of white, then it needs to be globaled

print("Here's an empty stack")
print(stackArray)

def push(newItem):
    global topPointer, stackSize
    if topPointer < (stackSize-1):
        topPointer = topPointer + 1
        stackArray[topPointer] = newItem
        print("here's the stack after a push")
        print(stackArray)
    else:
        print("stop pushing bro the stack is already full")

def pop():
    global topPointer, nullPointer, emptyString
    if topPointer > nullPointer:
        stackArray[topPointer] = emptyString
        topPointer = topPointer - 1
        print("here's the stack after a pop")
        print(stackArray)
    else:
        print("stack is empty bro what are you popping")

# instruction: push 7, push 32, pop twice, pop another time to see what happens if you pop an empty stack
# push numbers 1 until 10, try to push 11 even tho stack is full

push(7)
push(32)
pop()
pop()
pop()

# if you write for x in range (1,10) will yield numbers 1 until 9 only. but we want 1 until 10
# hence we write for x in range (1,11)

for x in range (1,11):
    push(x)

push(11)
