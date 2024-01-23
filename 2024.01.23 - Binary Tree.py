# use of recursive. a node is a parent relative to its child node. the child could be a parent itself relative to its own child.
# outputting the nodes could either be in order, preorder or postorder
class Node:
    def __init__(self, item):
        self.__leftNode = None
        self.__rightNode = None
        self.__item = item  # root or parent node

    def insertItem(self, item):
        if item < self.__item:  # items less than root/parent
            if self.__leftNode is None:  # if left node is empty
                self.__leftNode = Node(item)  # assign the new item to teh empty left node
            else:  # if left node isn't empty
                self.__leftNode.insertItem(item)  # recursively, the left node becomes a "parent"
        elif item > self.__item:  # items larger than root/parent
            if self.__rightNode is None:
                self.__rightNode = Node(item)
            else:
                self.__rightNode.insertItem(item)
        else:
            self.__item = item  # if new item has the same value as root/parent, replace itself with itself

    def inOrderTraversal(self):
        if self.__leftNode is not None:
            self.__leftNode.inOrderTraversal()
        print(self.__item)
        if self.__rightNode is not None:
            self.__rightNode.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.__item)
        if self.__leftNode is not None:
            self.__leftNode.preOrderTraversal()
        if self.__rightNode is not None:
            self.__rightNode.preOrderTraversal()

    def postOrderTraversal(self):
        if self.__leftNode is not None:
            self.__leftNode.postOrderTraversal()
        if self.__rightNode is not None:
            self.__rightNode.postOrderTraversal()
        print(self.__item)

    def searchItem(self, Item):
        if Item == self.__item:
            return self.__item  # return the item found
        elif (Item < self.__item) and (self.__leftNode is not None):
            return self.__leftNode.searchItem(Item)
        elif (Item > self.__item) and (self.__rightNode is not None):
            return self.__rightNode.searchItem(Item)
        else:
            return None  # return None if not found

# the position of the item printed affects in, pre, or post order output

myTree = Node(27)  # setting a tree where the root is 27
myTree.insertItem(24)  # inserting new nodes
myTree.insertItem(25)
myTree.insertItem(30)
print("Here is the output using In Order Traversal:")
myTree.inOrderTraversal()
print("Here is the output using Pre Order Traversal:")
myTree.preOrderTraversal()
print("Here is the output using Post Order Traversal:")
myTree.postOrderTraversal()
print("")

#  let's try searching for an item

if myTree.searchItem(25) == None:
    print("Item does not exist")
else:
    print(myTree.searchItem(25))
