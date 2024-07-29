'''
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: 
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be 
partitioned into two such parts. '''

class Solution:
    def equalPartition(self, N, nums):
        # code here
         total_sum = sum(nums)
        
        # Check if the total sum is odd, in which case it's impossible to partition
        if total_sum % 2:
            return False
        
        # Calculate the target sum for each partition
        target_sum = total_sum // 2
        
        dp = [1 if i == 0 else 0 for i in range(target_sum + 1)]
        
        for num in nums:
            achieved_sums = set()
            
            for j in range(num, target_sum + 1):
               
                if dp[j] == 0 and dp[j - num] and (j - num) not in achieved_sums:
                    dp[j] = 1
                    achieved_sums.add(j)
                # If the target sum is achieved, return True
                if dp[target_sum]:
                    return 1
        
        # If no partition is found, return False
        return 0