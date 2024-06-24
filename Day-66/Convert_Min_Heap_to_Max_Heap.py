''' You are given an array arr of N integers representing a min Heap. The task is to convert it to max Heap.

A max-heap is a complete binary tree in which the value in each internal node is greater than or equal to the values in the children of that node. 

Example 1:

Input:
N = 4
arr = [1, 2, 3, 4]
Output:
[4, 2, 3, 1]
Explanation:

The given min Heap:

          1
        /   \
      2       3
     /
   4

Max Heap after conversion:

         4
       /   \
      2     3
    /
   1
Example 2:

Input:
N = 5
arr = [3, 4, 8, 11, 13]
Output:
[13, 11, 8, 3, 4]
Explanation:

The given min Heap:

          3
        /   \
      4      8
    /   \ 
  11     13

Max Heap after conversion:

          13
        /    \
      11      8
    /   \ 
   3     4 '''



   class Solution:
    def convertMinToMaxHeap(self, N, arr):
        # Code here
        for i in range(N//2, -1, -1):
            self.heapify_down(i, arr)
            
            
    def heapify_down(self,i,arr):
        # global arr
        large = i
        l = 2*i + 1
        r = 2*i + 2
        if l<len(arr) and arr[l]>arr[large]:
            large = l
        if r<len(arr) and arr[r]>arr[large]:
            large = r
        if large != i:
            arr[large],arr[i] = arr[i],arr[large]
            self.heapify_down(large,arr)