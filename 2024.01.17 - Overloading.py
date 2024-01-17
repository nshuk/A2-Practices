class greeting:
    def hello(self, firstname = None, lastname = None):
        if (firstname != None) and (lastname != None):
            print("Hello", firstname, lastname)
        elif (firstname != None):
            print("Hello", firstname)
        else:
            print("Hello")

myGreeting = greeting()
myGreeting.hello("Naqib", "Shukri")
myGreeting.hello("Naqib")
myGreeting.hello()

# at line 2, what it means by firstname = None is that the spot is initialized to be empty if no parameter is passed to
# that spot
# at line 3, the condition is firstname <> none and lastname <> none, what this means is, if the spots is given a
# parameter in other words it's not none, then the condition is met