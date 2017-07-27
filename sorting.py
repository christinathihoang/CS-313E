#   File: sorting.py
#   Description: This program is a driver that calculates the execution time of four different sorting algorithms.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 7/26/2017
#   Date Last Modified: 7/28/2017

import random
import time
import sys

sys.setrecursionlimit(10000)

# bubble sort algorithm
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# insertion sort algorithm
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

# merge sort algorithm
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

# quick sort algorithm
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def main():

    # calculate average executive time for four sorting algorithms using randomly sorted lists

    # stores average sort times for n length lists
    bubbleSortAvgList = []
    insertionSortAvgList = []
    mergeSortAvgList = []
    quickSortAvgList = []
    
    for n in [10, 100, 1000]:
        
        bubbleSortTime = []
        insertionSortTime = []
        mergeSortTime = []
        quickSortTime = []        

        # for five trials
        for i in range(0,5):

            # create and randomly shuffle n length list
            numList = [y for y in range(0, n)]
            random.shuffle(numList)
             
            # calculates time for bubble sort
            startTime = time.perf_counter()
            bubbleSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            bubbleSortTime.append(elapsedTime) 
          
            # calculate time for insertion sort
            startTime = time.perf_counter()
            insertionSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            insertionSortTime.append(elapsedTime)
          
            # calculates time for merge sort
            startTime = time.perf_counter()
            mergeSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            mergeSortTime.append(elapsedTime)

            # calculates time for quick sort
            startTime = time.perf_counter()
            quickSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            quickSortTime.append(elapsedTime)

        # calculates average time of five trials and stores in list
        bubbleSortAvg = sum(bubbleSortTime)/5
        bubbleSortAvgList.append(bubbleSortAvg)

        insertionSortAvg = sum(insertionSortTime)/5
        insertionSortAvgList.append(insertionSortAvg)
            
        mergeSortAvg = sum(mergeSortTime)/5
        mergeSortAvgList.append(mergeSortAvg)
            
        quickSortAvg = sum(quickSortTime)/5
        quickSortAvgList.append(quickSortAvg)

    # print results
    print("Input type = Random")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort   ", "%f"%bubbleSortAvgList[0]," ","%f"%bubbleSortAvgList[1]," ","%f"%bubbleSortAvgList[2])
    print("   insertionSort   ", "%f"%insertionSortAvgList[0]," ","%f"%insertionSortAvgList[1]," ","%f"%insertionSortAvgList[2])
    print("       mergeSort   ", "%f"%mergeSortAvgList[0]," ","%f"%mergeSortAvgList[1]," ","%f"%mergeSortAvgList[2])
    print("       quickSort   ", "%f"%quickSortAvgList[0]," ","%f"%quickSortAvgList[1]," ","%f"%quickSortAvgList[2])

    # calculate average execution time for four sorting algorithms using sorted lists
    bubbleSortAvgList = []
    insertionSortAvgList = []
    mergeSortAvgList = []
    quickSortAvgList = []
    
    # calculate average execution time for four sorting algorithms using sorted lists
    for n in [10, 100, 1000]:
        
        bubbleSortTime = []
        insertionSortTime = []
        mergeSortTime = []
        quickSortTime = []        

        for i in range(0,5):

            # creates n length sorted list
            numList = [y for y in range(0, n)]
             
            # calculates time for bubble sort
            startTime = time.perf_counter()
            bubbleSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            bubbleSortTime.append(elapsedTime) 
          
            # calculate time for insertion sort
            startTime = time.perf_counter()
            insertionSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            insertionSortTime.append(elapsedTime)
          
            # calculates time for merge sort
            startTime = time.perf_counter()
            mergeSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            mergeSortTime.append(elapsedTime)

            # calculates time for quick sort
            startTime = time.perf_counter()
            quickSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            quickSortTime.append(elapsedTime)

        # calculates average time of five trials and stores in list
        bubbleSortAvg = sum(bubbleSortTime)/5
        bubbleSortAvgList.append(bubbleSortAvg)

        insertionSortAvg = sum(insertionSortTime)/5
        insertionSortAvgList.append(insertionSortAvg)
            
        mergeSortAvg = sum(mergeSortTime)/5
        mergeSortAvgList.append(mergeSortAvg)
            
        quickSortAvg = sum(quickSortTime)/5
        quickSortAvgList.append(quickSortAvg)

    # print results
    print("\n")
    print("Input type = Sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort   ", "%f"%bubbleSortAvgList[0]," ","%f"%bubbleSortAvgList[1]," ","%f"%bubbleSortAvgList[2])
    print("   insertionSort   ", "%f"%insertionSortAvgList[0]," ","%f"%insertionSortAvgList[1]," ","%f"%insertionSortAvgList[2])
    print("       mergeSort   ", "%f"%mergeSortAvgList[0]," ","%f"%mergeSortAvgList[1]," ","%f"%mergeSortAvgList[2])
    print("       quickSort   ", "%f"%quickSortAvgList[0]," ","%f"%quickSortAvgList[1]," ","%f"%quickSortAvgList[2])

    
    # calculate average execution time for four sorting algorithms using reverse sorted lists
    bubbleSortAvgList = []
    insertionSortAvgList = []
    mergeSortAvgList = []
    quickSortAvgList = []
    
    for n in [10, 100, 1000]:
        
        bubbleSortTime = []
        insertionSortTime = []
        mergeSortTime = []
        quickSortTime = []        

        for j in range(0,5):

            # create n length list in reverse order
            numList = [y for y in range(n,0,-1)]
             
            # calculates time for bubble sort
            startTime = time.perf_counter()
            bubbleSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            bubbleSortTime.append(elapsedTime) 
          
            # calculate time for insertion sort
            startTime = time.perf_counter()
            insertionSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            insertionSortTime.append(elapsedTime)
          
            # calculates time for merge sort
            startTime = time.perf_counter()
            mergeSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            mergeSortTime.append(elapsedTime)

            # calculates time for quick sort
            startTime = time.perf_counter()
            quickSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            quickSortTime.append(elapsedTime)

        # calculates average time of five trials and stores in list
        bubbleSortAvg = sum(bubbleSortTime)/5
        bubbleSortAvgList.append(bubbleSortAvg)

        insertionSortAvg = sum(insertionSortTime)/5
        insertionSortAvgList.append(insertionSortAvg)
            
        mergeSortAvg = sum(mergeSortTime)/5
        mergeSortAvgList.append(mergeSortAvg)
            
        quickSortAvg = sum(quickSortTime)/5
        quickSortAvgList.append(quickSortAvg)

    # print results
    print("\n")
    print("Input type = Reverse")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort   ", "%f"%bubbleSortAvgList[0]," ","%f"%bubbleSortAvgList[1]," ","%f"%bubbleSortAvgList[2])
    print("   insertionSort   ", "%f"%insertionSortAvgList[0]," ","%f"%insertionSortAvgList[1]," ","%f"%insertionSortAvgList[2])
    print("       mergeSort   ", "%f"%mergeSortAvgList[0]," ","%f"%mergeSortAvgList[1]," ","%f"%mergeSortAvgList[2])
    print("       quickSort   ", "%f"%quickSortAvgList[0]," ","%f"%quickSortAvgList[1]," ","%f"%quickSortAvgList[2])

    
    # calculate average execution time for four sorting algorithms using almost sorted lists
    bubbleSortAvgList = []
    insertionSortAvgList = []
    mergeSortAvgList = []
    quickSortAvgList = []
    
    for n in [10, 100, 1000]:
        
        bubbleSortTime = []
        insertionSortTime = []
        mergeSortTime = []
        quickSortTime = []        

        for i in range(0,5):

            # creates n length sorted list
            numList = [y for y in range(n,0,-1)]
            x = int(0.1*len(numList))

            # randomly pops and inserts a number to create an almost sorted list
            for k in range(x):
                idx1, idx2 = random.sample(range(len(numList)),2)
                randomNum = numList.pop(idx1)
                numList.insert(idx2,randomNum)   

            # calculates time for bubble sort
            startTime = time.perf_counter()
            bubbleSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            bubbleSortTime.append(elapsedTime) 
          
            # calculate time for insertion sort
            startTime = time.perf_counter()
            insertionSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            insertionSortTime.append(elapsedTime)
          
            # calculates time for merge sort
            startTime = time.perf_counter()
            mergeSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            mergeSortTime.append(elapsedTime)

            # calculates time for quick sort
            startTime = time.perf_counter()
            quickSort(numList)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            quickSortTime.append(elapsedTime)

        # calculates average time of five trials and stores in list
        bubbleSortAvg = sum(bubbleSortTime)/5
        bubbleSortAvgList.append(bubbleSortAvg)

        insertionSortAvg = sum(insertionSortTime)/5
        insertionSortAvgList.append(insertionSortAvg)
            
        mergeSortAvg = sum(mergeSortTime)/5
        mergeSortAvgList.append(mergeSortAvg)
            
        quickSortAvg = sum(quickSortTime)/5
        quickSortAvgList.append(quickSortAvg)

    # print results
    print("\n")
    print("Input type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort   ", "%f"%bubbleSortAvgList[0]," ","%f"%bubbleSortAvgList[1]," ","%f"%bubbleSortAvgList[2])
    print("   insertionSort   ", "%f"%insertionSortAvgList[0]," ","%f"%insertionSortAvgList[1]," ","%f"%insertionSortAvgList[2])
    print("       mergeSort   ", "%f"%mergeSortAvgList[0]," ","%f"%mergeSortAvgList[1]," ","%f"%mergeSortAvgList[2])
    print("       quickSort   ", "%f"%quickSortAvgList[0]," ","%f"%quickSortAvgList[1]," ","%f"%quickSortAvgList[2])

main()