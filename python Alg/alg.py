"""
Linear Search
Binary Search
Bubble Sort
Insertion Sort
Quick Sort

Stack
Queue
Linked List
Binary Tree
"""
def linearSearch(target, anList):
    size = len(anList)
    position = 0
    while position < size:
        if anList[position] == target:
            break
        position += 1
    return position

def binarySearch(self, target, anList):
    anList.sort()
    size = len(anList)
    start, end = 0, size - 1
    while start + 1 < end:
        mid = start + (end - start) / 2
        if anList[mid] == target:
            return mid
        elif anList[mid] > target:
            end = mid
        else:
            end = start
    if anList[start] == target:
        return start
    elif anList[end] == target:
        return end
    return -1

def bubbleSort(array):
    pass


def mergeSort(anList):
    pass

def quickSort(anList):
    pass

def insertionSort(anList):
    size = len(anList)
    curr = 1
    while curr < size - 1:
        currnum = anList[curr]

