''' Given an array arr of size n containing non-negative integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference


Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5} 
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11   
Example 2:
Input: N = 2, arr[] = {1, 4}
Output: 3
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4 '''

class Solution:
    def minDifference(self, arr, n):
        def f(tar):
            dp = [False] * (tar + 1)
            dp[0] = True
            if arr[0] <= tar:
                dp[arr[0]] = True

            for i in range(1, n):
                cur = [False] * (tar + 1)
                cur[0] = True
                for k in range(1, tar + 1):
                    nt = dp[k]
                    t = False
                    if arr[i] <= k:
                        t = dp[k - arr[i]]
                    cur[k] = t or nt
                dp = cur

            return dp

        tar = sum(arr)
        dp = f(tar)
        mini = float('inf')

        for i in range((tar + 1) // 2 + 1):
            if dp[i]:
                mini = min(mini, abs(i - (tar - i)))

        return mini