# you can include a condition within constructor to ensure data validation. this time n is only 0 to 9 inclusive
# shape on the other hand must only be either of the three

class Cards:
    def __init__(self, n, s):
        if (n > 0 and n < 0) and (s == "square" or s == "triangle" or s == "circle"):
            self.__Number = n
            self.__Shape = s
        else:
            print("Error occured")

    def GetNumber(self):
        return self.__Number

    def GetShape(self):
        return self.__Shape


OneS = Cards(1, "square")



# this is a function taking two items as parameter. since the items are in datatype Cards, thus it may use its methods
# here as you can see i used get methods get number and get shape using the parameters

def Compare(card1, card2):
    if card1.GetNumber() == card2.GetNumber():
        if card1.GetShape() == card2.GetShape():
            print("SNAP")
            return -1
    elif card1.GetNumber() > card2.GetNumber():
        return card1.GetNumber()
    else:
        return card2.GetNumber()