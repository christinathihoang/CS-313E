import sys

# create queue
class Queue:

    # init method
    def __init__(self):
        self.items = []

    # str method
    def __str__(self):
        return str(self.items)

    # add an item to the front of the queue, arg item, returns none
    def enqueue(self,item):
        return self.items.insert(0, item)

    # remove an item from front, no args, returns item removed
    def dequeue(self):
        return self.items.pop(-1)

    # checks to see if queue is empty, returns boolean
    def isEmpty(self):
        return self.items == []

    # returns number of items in a queue
    def size(self):
        return len(self.items)

    # returns item at the front of the queue without changing queue, no arguments, returns item
    def peek(self):
        return self.items[0]

def main():

    # initialize queues for three categories of conditions
    critical = Queue()
    serious = Queue()
    fair = Queue()

    # open file
    infile = open("ERsim.txt","r")
    
    # go through each command line in file
    for line in infile:

        # split command line and assign variable names
        commandLine = line.split()
        command = commandLine[0]
        if len(commandLine) == 3:
            condition = commandLine[1]
            patient = commandLine[2]

        # determine and treat the next patient
        if commandLine[0] == "treat" and commandLine[1] == "next":

            # print command
            print("Command: Treat next patient")
            print("\n")

            # pop patient name from queue, in order of severity
            if not critical.isEmpty():
                print("   Treating",critical.dequeue(),"from Critical queue")
            elif not serious.isEmpty():
                print("   Treating",serious.dequeue(),"from Serious queue")
            elif not fair.isEmpty():
                print("   Treating",fair.dequeue(),"from Fair queue")

            # print updated queues
            if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                print("   No patients in queues")
                print("\n")
            else:
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical)
                print("\n")


        #treat all patients
        elif commandLine[0] == "treat" and commandLine[1] == "all":

            # print command
            print("Command: Treat all patients")
            print("\n")

            # pop patient name from queue in order of severity, until all queues are empty
            while not critical.isEmpty():
                print("   Treating",critical.dequeue(),"from Critical queue")
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical)
                print("\n")
            while not serious.isEmpty():
                print("   Treating",serious.dequeue(),"from Serious queue")
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical) 
                print("\n")     
            while not fair.isEmpty():
                print("   Treating",fair.dequeue(),"from Fair queue")
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical)
                print("\n")

            # print updated queues
            if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                print("   No patients in queues")
                print("\n")

        # treat the next patient in a specified queue
        elif command == "treat":

            # print command
            print("Command: Treat next patient on",condition,"queue")
            print("\n")

            # pop patient name from specified queue
            if condition == "Critical":
                if not critical.isEmpty:
                    print("   Treating",critical.dequeue(),"from Critical queue")
                else: 
                    print("   No patients available in queue")
            elif condition == "Serious":
                if not serious.isEmpty():
                    print("   Treating",serious.dequeue(),"from Serious queue")
                else:
                    print("   No patients available in queue")
            elif condition == "Fair":
                if not fair.isEmpty():
                    print("   Treating",fair.dequeue(),"from Fair queue")
                else:
                    print("   No patients available in queue")

            # print updated queues
            if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                print("   No patients in queues")
                print("\n")
            else:
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical)
                print("\n")

        # add a patient to the appropriate queue
        elif command == "add":

            # print patient being added to which queue
            print("Command: Add patient",patient,"to",condition,"queue")
            print("\n")

            # add patient to each designated queue
            if condition == "Critical":
                critical.enqueue(patient)
            elif condition == "Serious":
                serious.enqueue(patient)
            elif condition == "Fair":
                fair.enqueue(patient)

            # print updated queues
            print("   Queues are:")
            if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                print("   No patients in queues")
                print("\n")
            else:
                print("   Fair:    ",fair)
                print("   Serious: ",serious)
                print("   Critical:",critical)
                print("\n")
        
        # exit program
        elif command == "exit":
            print("Command: Exit")
            sys.exit()

main()