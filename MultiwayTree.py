#   File: MultiwayTree.py
#   Description: This program creates N-ary trees from Python expressions and compares two trees for isomorphism.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 8/5/2017
#   Date Last Modified: 8/8/2017

# create multiway tree class
class MultiwayTree():

    def __init__(self, pyTree):                                     # recursively create multiway tree
        self.data = pyTree
        self.children = []
        self.parent = None
        self.root = None

        self.setRootVal(self.data[0])
        for i in range(len(self.data[1])):
            self.insertChild(self.data[1][i])

    def setRootVal(self, value):                                    # changes pointer
        self.root = value

    def getRootVal(self):                                           # returns pointer
        return self.root

    def getChildren(self):                                          # returns list of children
        return self.children

    def sizeChildren(self):                                         # returns size of list of children
        return len(self.children)

    def insertChild(self, child):                                   # inserts tree as child
        t = MultiwayTree(child)
        self.children.append(t)
        t.parent = self

    def preOrder(self):                                             # preorder expression method
        print(self.root, end = " ")
        if self.children != None:
            for child in self.getChildren():
                child.preOrder()

    def isIsomorphicTo(self, other):
        try:
            if self.children == [] and other.children == []:        # base case for isomorphic trees
                return True
            elif self.children == [] or other.children == []:       # base case for non isomorphic trees
                return False
            elif self.children != [] and other.children != []:      # recursion
                isomorphic = True
                for i in range(self.sizeChildren()):
                    selfChild = self.children[i]
                    otherChild = other.children[i]
                    isomorphic = isomorphic and selfChild.isIsomorphicTo(otherChild)
                return isomorphic
        except IndexError:
            return False
       
def main():
    infile = open("MultiwayTreeInput.txt", "r")     # open file and count number of lines
    lineNum = sum(1 for _ in infile)
    infile.close()

    infile = open("MultiwayTreeInput.txt", "r")     # open file
    tree = 0

    # iterate through file 
    for i in range(0, lineNum-1, 2):
        line1 = infile.readline()                   # read two lines from file at a time
        line2 = infile.readline()
        t1 = MultiwayTree(eval(line1))              # create first tree

        tree += 1
        print("Tree",tree,":", t1.data)
        print("Tree",tree,":",end = " ")            # print preorder expression for first tree
        t1.preOrder()
        print("\n")
        
        tree += 1
        t2 = MultiwayTree(eval(line2))              # create second tree
        print("Tree",tree,":", t2.data)
        print("Tree",tree,":",end = " ")            # print preorder expression for second tree
        t2.preOrder()
        print("\n")

        if t1.isIsomorphicTo(t2):                   # compare trees for isomorphism
            print("Tree",(tree-1),"is isomorphic to Tree",tree)
        else:
            print("Tree",(tree-1),"is not isomorphic to Tree",tree)
        print("\n")

    infile.close()
main()