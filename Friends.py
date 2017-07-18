#   File: Friends.py
#   Description: This program implements the "friend" functionality of a Facebook-like application.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 7/14/2017
#   Date Last Modified: 7/17/2017

import sys

class Node():                           # create Node class

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

class LinkedList():                     # create Linked List class

    def __init__(self):
        self.head = None

    def __str__(self):                  # str method
        current = self.head
        linkedList = "[ "               # initializes an empty string
        counter = 0
        end = False

        while current != None:                          # loop continues until the last node
            linkedList += current.getData() + " "       # adds element to string with two spaces between each
            counter += 1
            current = current.getNext()                 # get next element
        linkedList += "]"

        return linkedList 

    def add(self, item):                                # add element to the beginning of the list
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

   
    def find(self, item):                               # checks if element is in list, returns boolean
        current = self.head
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found


    def delete(self, item):                              # finds item and deletes from list                  
        current = self.head
        previous = None
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
                if previous == None:                    
                    self.head = current.getNext()
                elif current.getNext() == None:
                    previous.setNext(None)
                else:
                    previous.setNext(current.getNext())
            else:
                previous = current
                current = current.getNext()


    def isEmpty(self):                                    # checks if list is empty, returns boolean
        return self.head == None

class User():                               # creates User class

    def __init__(self, name):
        self.name = name
        self.friends = LinkedList()

    def __str__(self):
        return str(self.name)

    def addFriend(self, friend):            # add user account to friend list
        self.friends.add(friend)

    def deleteFriend(self, friend):         # deletes user account from friend list
        self.friends.delete(friend)

    def findFriend(self, friend):           # finds user account in friend list, returns boolean
        return self.friends.find(friend)

def findAccount(userList, name):            # finds and returns instance of user stored in linked list
    current = userList.head
    while current is not None:
        if current.getData().name == name:
            return current.getData()
        else:
            current = current.getNext()
    return None

def main():

    infile = open("FriendData.txt", "r")    # open file

    userList = LinkedList()                 # create linked list to store all user instances

    for line in infile:                     # interate through each command in the file
        print("-->",line)
        line = line.split()                 # split command line
        command = line[0]
        if len(line) == 2:
            name1 = line[1]
        elif len(line) == 3:
            name1 = line[1]
            name2 = line[2]

        if command == "Person":                                             # create new user account
            if findAccount(userList, name1) == None:                                   
                name = User(name1)                                          # initialize instance of User class             
                userList.add(name)                                          # add account to unordered linked list                
                print("   ",name1,"now has an account.")   
            else:
                print("    A person with name",name1,"already exists.")

        elif command == "Friend":                                           # add friend by adding users to each other's friend list
            if name1 == name2:
                print("    A person cannot friend himself/herself.")
            elif findAccount(userList, name1) == None:
                print("    A person with name",name1,"does not currently exist.")
            elif findAccount(userList, name2) == None:
                print("    A person with name",name2,"does not currently exist.")
            elif findAccount(userList, name1).findFriend(name2):
                print("   ",name1,"and",name2,"are already friends.")
            else:
                if findAccount(userList, name1) != None:                     # add friend 2
                    findAccount(userList, name1).addFriend(name2)
                if findAccount(userList, name2) != None:                     # add friend 1
                    findAccount(userList, name2).addFriend(name1)
                print("   ",name1,"and",name2,"are now friends.")


        elif command == "Unfriend":                                           # unfriend by removing users from each other's friend list
            if name1 == name2:
                print("    A person cannot unfriend himself/herself.")
            elif findAccount(userList, name1) == None:
                print("    A person with name",name1,"does not currently exist.")
            elif findAccount(userList, name2) == None:
                print("    A person with name",name2,"does not currently exist.")
            elif not findAccount(userList, name1).findFriend(name2):
                print("   ",name1,"and",name2,"aren't friends, so you can't unfriend them.")
            else:
                if findAccount(userList, name1) != None:                       # delete friend 2
                    findAccount(userList, name1).deleteFriend(name2)
                if findAccount(userList, name2) != None:                       # delete friend 1
                    findAccount(userList, name2).deleteFriend(name1)
                print("   ",name1,"and",name2,"are no longer friends.")
       

        elif command == "List":                                                 # print all friends
            if findAccount(userList, name1).friends.isEmpty():
                print("   ",name1,"has no friends.")
            else:
                print("   ",findAccount(userList, name1).friends)

        elif command == "Query":                                                # search friends for a specific user
            if name1 == name2:
                print("    A person cannot query himself/herself.") 
            elif findAccount(userList, name1) == None:
                print("    A person with name",name1,"does not currently exist.")
            elif findAccount(userList, name2) == None:
                print("    A person with name",name2,"does not currently exist.")
            elif findAccount(userList, name1).findFriend(name2):
                print("   ",name1,"and",name2,"are friends.")
            elif not findAccount(userList, name1).findFriend(name2):
                print("   ",name1,"and",name2,"are not friends.")

        elif command == "Exit":                                                 # exit program
            print("    Exiting...")
            infile.close()
            sys.exit()

        print("\n")

main()