'''  Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
Example 2:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0 
Explanation: There is no subset with sum 30. '''

class Solution:
    def isSubsetSum (self, N, nums, sum):
        # code here 
        dp=set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            new_dp=set()
            for t in dp:
                if t+nums[i]==sum:
                    return True
                new_dp.add(t+nums[i])
                new_dp.add(t)
            dp=new_dp

        return True if sum in dp else False
        
