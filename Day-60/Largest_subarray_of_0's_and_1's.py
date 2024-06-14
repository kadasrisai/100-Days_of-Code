'''Given an array of 0s and 1s. Find the length of the largest subarray with equal number of 0s and 1s.

Example 1:

Input:
N = 4
A[] = {0,1,0,1}
Output: 4
Explanation: The array from index [0...3]
contains equal number of 0's and 1's.
Thus maximum length of subarray having
equal number of 0's and 1's is 4.
Example 2:

Input:
N = 5
A[] = {0,0,1,0,0}
Output: 2'''
class Solution:
    def maxLen(self,arr, N):
        # code here
        hash = {}
        sum = 0
        max_len = 0
        
        for i in range(N):
            if arr[i] == 0:
                arr[i] = -1  
            sum += arr[i]
            
            if sum == 0:
                max_len = i + 1 #increment the max lenght
            
            if sum in hash:
                max_len = max(max_len,i-hash[sum]) # arr[i] stored in -1 subtract it in sum
            else:
                hash[sum] = i
        return max_len