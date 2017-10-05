import sys

#Binary search
'''
Binary Search 部分 
Time: O(logn)
模版:
start + 1 < end
start + (end - start) / 2
A[mid] ==, <, >
A[start] A[end] ? target
经典题目
'''
# Binary search
class BinarySearch:
    def binarySearch(self, arraylist, target):
        if arraylist == None or len(arraylist) == 0: 
            return -1
        
        left, right = 0, len(arraylist)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if target == arraylist[mid]:
                return mid
            elif target < arraylist[mid]:
                right = mid
            else:
                left = mid
        if arraylist[left] != target:
            if arraylist[right] != target:
                return -1
            else:
                return right
        return left
        


# Binary Tree & Divide Conquer

        
# BFS
'''

'''
class BFS:
    def bfs(self, root, target):



# DFS
'''

'''
class DFS:
    def dfs(self, ):
        


# linked list and array

# Hash & Heap

#Two Pointers

#Dynamic Programming

