''' Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

Examples:

Input: arr[] = {1,2,3,7,5}, n = 5, s = 12
Output: 2 4
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = {1,2,3,4,5,6,7,8,9,10}, n = 10, s = 15,
Output: 1 5
Explanation: The sum of elements from 1st to 5th position is 15.'''
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        allsum,start=0,0
        for i in range(n):
            allsum+=arr[i]
            while(allsum>s and start<i):
                allsum-=arr[start]
                start=start+1
            if(allsum==s):
                return [start+1,i+1]
        return [-1]
