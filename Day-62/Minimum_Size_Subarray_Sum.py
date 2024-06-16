'''Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0'''

class Solution:
    def func(self, mid, k, v):
        n = len(v)
        sum_ = 0
        for i in range(mid):
            sum_ += v[i]
        if sum_ >= k:
            return True
        
        for i in range(mid, n):
            sum_ += v[i] - v[i - mid]
            if sum_ >= k:
                return True
        
        return False

    def minSubArrayLen(self, t, v):
        n = len(v)
        s = 0
        ans = s
        e = n
        while s <= e:
            mid = (s + e) // 2
            if self.func(mid, t, v):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans