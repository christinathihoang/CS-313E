#   File: ExpressionTree.py
#   Description: This program evaluates mathematical expressions using binary trees.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 7/30/2017
#   Date Last Modified: 8/2/2017

# create Stack class
class Stack (object):

    def __init__(self):                                                 # return list of items
        self.items = []

    def isEmpty (self):                                                 # checks if list is empty and returns boolean
        return self.items == []

    def push (self, item):                                              # appends item to the front of the list
        self.items.append(item)

    def pop (self):                                                     # pops off top item
        return self.items.pop()

    def peek (self):                                                    # shows top item
        return self.items[-1]

    def size (self):                                                    # returns number of items in the list
        return len(self.items)

# create Binary Tree class
class BinaryTree():

    def __init__(self, initVal = None):                                 # init method
        self.data = initVal
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

    def insertLeft(self, newNode):                                      # insert binary tree as a left node
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):                                     # insert binary tree as a right node
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getLeftChild(self):                                             # returns a pointer
        return self.left

    def getRightChild(self):                                            # returns a pointer
        return self.right

    def setRootVal(self, value):                                        # changes a pointer
        self.data = value

    def getRootVal(self):                                               # changes a pointer
        return self.data

    def createTree(self, expr):                                         # create binary tree method
        line = expr.split()                                             # splits expression    
        operator = ["+", "-", "*", "/"]
        parent = Stack()                                                # initialize parent stack
        for token in line:
            if token == "(":
                if self.left == None:
                    self.insertLeft(None)                               # add new node as the left child of the current node
                    parent.push(self)
                    self = self.getLeftChild()                          # change current node to the new node
            elif token == ")":
                if not parent.isEmpty():
                    self = parent.pop()                                 # set current node equal to the parent node
            elif token in operator:
                self.setRootVal(token)                                  # set current node's data value to the operator
                self.insertRight(None)                                  # add new node as right child of the current node
                parent.push(self)
                self = self.getRightChild()                             # change the current node to the new node
            else:
                self.setRootVal(token)                                  # set the current node's data value to the operand
                self = parent.pop()                                     # make the current node equal to the parent

    def evaluate(self):                                                                     # this method recursively evaluates the expression and returns a float
        operator = ["+", "-", "*", "/"]
        if self.getRootVal() is None:                                                       # base case; find the lowest leaf node
            return 0
        elif self.getRootVal() not in operator:
            return float(self.getRootVal())
        elif self.getRootVal() == "+":
            return self.getLeftChild().evaluate() + self.getRightChild().evaluate()
        elif self.getRootVal() == "-":
            return self.getLeftChild().evaluate() - self.getRightChild().evaluate()
        elif self.getRootVal() == "*":
            return self.getLeftChild().evaluate() * self.getRightChild().evaluate()
        elif self.getRootVal() == "/":
            return self.getLeftChild().evaluate() / self.getRightChild().evaluate()
    
    def preOrder(self):                                                                     # returns the prefix notation for expression

        if self.data != "(" and self.data != ")":                                           # don't print parentheses
            print(self.data, end = " ")
        if self.left != None:                                                               # first go through and print all left children until the lowest left leaf node is reached 
            self.getLeftChild().preOrder()
        if self.right != None:                                                              # go back up to 
            self.getRightChild().preOrder()


    def postOrder(self):                                                                    # returns the postfix notation for the epression

        if self.left != None:
            self.getLeftChild().postOrder()
        if self.right != None:
            self.getRightChild().postOrder()
        if self.data != "(" and self.data != ")":
            print(self.data, end = " ")

def main():
    infile = open("treedata.txt","r")

    for line in infile:
        print("Infix expression:",line)
        t = BinaryTree(None)
        t.createTree(line)

        if t.evaluate()-int(t.evaluate()) == 0:                                             # print integer value if 0 is after the decimal
            print("   Value:",int(t.evaluate()))
        else:
            print("   Value:",t.evaluate())                                                 # print float value
        print("   Prefix expression:", end = " ")                                           # print prefix notation for expression
        t.preOrder()
        print("\n","  Postfix expression:", end = " ")                                      # print postfix notation for expression
        t.postOrder()
        print("\n")

    infile.close()
main()