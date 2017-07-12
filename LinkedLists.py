#   File: LinkedLists.py
#   Description: This program creates a linked list class with related methods and function.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 7/8/2017
#   Date Last Modified: 7/10/2017

# create node class
class Node():

    def __init__(self, initdata):       # init method
        self.data = initdata
        self.next = None

    def getData(self):                  # returns a POINTER
        return self.data

    def getNext(self):                  # returns a POINTER
        return self.next

    def setData(self, newData):         # changes a POINTER
        self.data = newData

    def setNext(self, newNext):         # changes a POINTER
        self.next = newNext

# create a linked list class
class LinkedList():

    def __init__(self):                 # init method
        self.head = None


    def __str__(self):                  # str method
        current = self.head
        linkedList = ""                 # initializes an empty string
        counter = 0
        end = False

        while current != None:                          # loop continues until the last node
            linkedList += current.getData() + "  "      # adds element to string with two spaces between each
            counter += 1

            if counter % 10 == 0:       # each iine only has 10 elements
                linkedList += "\n"

            current = current.getNext()

        return linkedList

    def addFirst(self, item):           # add element to beginning of the list
        temp = Node(item)               # initialize node with new item
        temp.setNext(self.head)
        self.head = temp


    def addLast(self, item):            # add element to end of the list
        current = self.head
        previous = None
        temp = Node(item)               # initialize node with new item

        while current != None:          # loop continues until the last node
            previous = current
            current = current.getNext()

        if previous == None:            # there are currently no elements in the list
            self.head = temp            # makes new node the head
        else:
            previous.setNext(temp)      # adds new node to the end


    def addInOrder(self, item):         # add element to ordered list, in order
        current = self.head
        previous = None
        temp = Node(item)               # initialize node
        stop = False

        while current != None and stop == False:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def getLength(self):                # return the number of items in the list
        current = self.head
        count = 0

        while current != None:          # interates through loop until the last node
            count += 1
            current = current.getNext()

        return count


    def findUnordered(self, item):      # checks if element is in list, returns boolean
        current = self.head
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def findOrdered(self, item):        # checks if element is in ordered list, returns boolean
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:        # utilizes ordered list
                    stop = True
                else:
                    current = current.getNext()

        return found


    def delete(self, item):                    # deletes item from list and returns boolean
        current = self.head
        previous = None
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
                if previous == None:                    # deletes item if it is the first element
                    self.head = current.getNext()
                elif current.getNext() == None:
                    previous.setNext(None)
                else:
                    previous.setNext(current.getNext())
            else:
                previous = current
                current = current.getNext()

        return found 


    def copyList(self):                 # copies linked list, returns new list
        copiedList = LinkedList()       # initialize copied list
        current = self.head

        while current != None:
            item = current.getData()
            copiedList.addLast(item)
            current = current.getNext()

        return copiedList


    def reverseList(self):              # reverses linked list, returns new list
        reversedList = LinkedList()     # initialize reversed list
        current = self.head

        while current != None:
            item = current.getData()
            reversedList.addFirst(item)
            current = current.getNext()
        return reversedList


    def orderList(self):                # orders a linked list alphabetically, returns new list
        orderedList = LinkedList()      # initialize ordered list
        current = self.head

        while current != None:
            item = current.getData()
            orderedList.addInOrder(item)
            current = current.getNext()

        return orderedList


    def isOrdered(self):                # checks if list is ordered, returns boolean
        previous = self.head
        current = previous.getNext()
        ordered = True

        if self.getLength() <= 1:
            return True
        else:
            while current != None and ordered:
                if previous.getData() > current.getData():
                    ordered = False
                else:
                    previous = current
                    current = current.getNext()

        return ordered


    def isEmpty(self):                      # checks if list is empty, returns boolean
        return self.head == None


    def mergeList(self, b):                 # merges two lists
        mergedList = self.copyList()        # creates a copy of the first list
        current = b.head

        while current != None:
            item = current.getData()
            mergedList.addInOrder(item)     # adds elements from second list, in order
            current = current.getNext()

        return mergedList

    def isEqual(self, b):                           # checks if two lists are the same, returns boolean
        current1 = self.head
        current2 = b.head
        equal = True

        if self.getLength() != b.getLength():       # checks for equal length
            return False

        while current1 != None and current2 != None and not equal:
            if current1 != current2:
                equal = False
            else:
                current1 = current1.getNext()
                current2 = current2.getNext()

        return equal


    def removeDuplicates(self):                     # remove duplicates from a list
        current = self.head
        unduplicatedList = LinkedList()             # initilize linked list of nonduplicates
        unduplicatedData = []                       # creates list of nonduplicates

        while current != None:
            item = current.getData()
            if item in unduplicatedData:
                current = current.getNext()
            else:
                unduplicatedData.append(item)
                unduplicatedList.addLast(item)
                current = current.getNext()

        return unduplicatedList


def main():

    print ("\n\n***************************************************************")
    print ("Test of addFirst:  should see 'node34...node0'")
    print ("***************************************************************")
    myList1 = LinkedList()
    for i in range(35):
        myList1.addFirst("node"+str(i))

    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of addLast:  should see 'node0...node34'")
    print ("***************************************************************")
    myList2 = LinkedList()
    for i in range(35):
        myList2.addLast("node"+str(i))

    print (myList2)

    print ("\n\n***************************************************************")
    print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
    print ("***************************************************************")
    greekList = LinkedList()
    greekList.addInOrder("gamma")
    greekList.addInOrder("delta")
    greekList.addInOrder("alpha")
    greekList.addInOrder("epsilon")
    greekList.addInOrder("omega")
    print (greekList)

    print ("\n\n***************************************************************")
    print ("Test of getLength:  should see 35, 5, 0")
    print ("***************************************************************")
    emptyList = LinkedList()
    print ("   Length of myList1:  ", myList1.getLength())
    print ("   Length of greekList:  ", greekList.getLength())
    print ("   Length of emptyList:  ", emptyList.getLength())

    print ("\n\n***************************************************************")
    print ("Test of findUnordered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
    print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

    print ("\n\n***************************************************************")
    print ("Test of findOrdered:  should see True, False")
    print ("***************************************************************")
    print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
    print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

    print ("\n\n***************************************************************")
    print ("Test of delete:  should see 'node25 found', 'node34 found',")
    print ("   'node0 found', 'node40 not found'")
    print ("***************************************************************")
    print ("   Deleting 'node25' (random node) from myList1: ")
    if myList1.delete("node25"):
       print ("      node25 found")
    else:
       print ("      node25 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node34' (first node) from myList1: ")
    if myList1.delete("node34"):
       print ("      node34 found")
    else:
       print ("      node34 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node0'  (last node) from myList1: ")
    if myList1.delete("node0"):
       print ("      node0 found")
    else:
       print ("      node0 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("   Deleting 'node40' (node not in list) from myList1: ")
    if myList1.delete("node40"):
       print ("      node40 found")
    else:
       print ("   node40 not found")
    print ("   myList1:  ")
    print (myList1)

    print ("\n\n***************************************************************")
    print ("Test of copyList:")
    print ("***************************************************************")
    greekList2 = greekList.copyList()
    print ("   These should look the same:")
    print ("      greekList before delete:")
    print (greekList)
    print ("      greekList2 before delete:")
    print (greekList2)
    greekList2.delete("alpha")
    print ("   This should only change greekList2:")
    print ("      greekList after deleting 'alpha' from second list:")
    print (greekList)
    print ("      greekList2 after deleting 'alpha' from second list:")
    print (greekList2)
    greekList.delete("omega")
    print ("   This should only change greekList1:")
    print ("      greekList after deleting 'omega' from first list:")
    print (greekList)
    print ("      greekList2 after deleting 'omega' from first list:")
    print (greekList2)

    print ("\n\n***************************************************************")
    print ("Test of reverseList:  the second one should be the reverse")
    print ("***************************************************************")
    print ("   Original list:")
    print (myList1)
    print ("   Reversed list:")
    myList1Rev = myList1.reverseList()
    print (myList1Rev) 

    print ("\n\n***************************************************************")
    print ("Test of orderList:  the second list should be the first one sorted")
    print ("***************************************************************")
    planets = LinkedList()
    planets.addFirst("Mercury")
    planets.addFirst("Venus")
    planets.addFirst("Earth")
    planets.addFirst("Mars")
    planets.addFirst("Jupiter")
    planets.addFirst("Saturn")
    planets.addFirst("Uranus")
    planets.addFirst("Neptune")
    planets.addFirst("Pluto?")
   
    print ("   Original list:")
    print (planets)
    print ("   Ordered list:")
    orderedPlanets = planets.orderList()
    print (orderedPlanets)

    print ("\n\n***************************************************************")
    print ("Test of isOrdered:  should see False, True")
    print ("***************************************************************")
    print ("   Original list:")
    print (planets)
    print ("   Ordered? ", planets.isOrdered())
    orderedPlanets = planets.orderList()
    print ("   After ordering:")
    print (orderedPlanets)
    print ("   ordered? ", orderedPlanets.isOrdered())

    print ("\n\n***************************************************************")
    print ("Test of isEmpty:  should see True, False")
    print ("***************************************************************")
    newList = LinkedList()
    print ("New list (currently empty):", newList.isEmpty())
    newList.addFirst("hello")
    print ("After adding one element:",newList.isEmpty())

    print ("\n\n***************************************************************")
    print ("Test of mergeList")
    print ("***************************************************************")
    list1 = LinkedList()
    list1.addLast("aardvark")
    list1.addLast("cat")
    list1.addLast("elephant")
    list1.addLast("fox")
    list1.addLast("lynx")
    print ("   first list:")
    print (list1)
    list2 = LinkedList()
    list2.addLast("bacon")
    list2.addLast("dog")
    list2.addLast("giraffe")
    list2.addLast("hippo")
    list2.addLast("wolf")
    print ("   second list:")
    print (list2)
    print ("   merged list:")
    list3 = list1.mergeList(list2)
    print (list3)

    print ("\n\n***************************************************************")
    print ("Test of isEqual:  should see True, False, True")
    print ("***************************************************************")
    print ("   First list:")
    print (planets)
    planets2 = planets.copyList()
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print (planets)
    planets2.delete("Mercury")
    print ("   Second list:")
    print (planets2)
    print ("      Equal:  ",planets.isEqual(planets2))
    print ("   Compare two empty lists:")
    emptyList1 = LinkedList()
    emptyList2 = LinkedList()
    print ("      Equal:  ",emptyList1.isEqual(emptyList2))

    print ("\n\n***************************************************************")
    print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
    print ("***************************************************************")
    dupList = LinkedList()
    print ("   removeDuplicates from an empty list shouldn't fail")
    newList = dupList.removeDuplicates()
    print ("   printing what should still be an empty list:")
    print (newList)
    dupList.addLast("giraffe")
    dupList.addLast("wolf")
    dupList.addLast("cat")
    dupList.addLast("elephant")
    dupList.addLast("bacon")
    dupList.addLast("fox")
    dupList.addLast("elephant")
    dupList.addLast("wolf")
    dupList.addLast("lynx")
    dupList.addLast("elephant")
    dupList.addLast("dog")
    dupList.addLast("hippo")
    dupList.addLast("aardvark")
    dupList.addLast("bacon")
    print ("   original list:")
    print (dupList)
    print ("   without duplicates:")
    newList = dupList.removeDuplicates()
    print (newList)

main()