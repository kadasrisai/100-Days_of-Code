''' Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.'''

class Solution(object):
    def __init__(self):
        self.ans = []
        self.sum = 0

    def dfs(self, cur, k, n, idx):
        if len(cur) == k and self.sum == n:
            self.ans.append(cur[:])  # Use cur[:] to create a copy of cur
            return
        elif len(cur) == k and self.sum > n:
            return
        
        for i in range(idx, 10):
            cur.append(i)
            self.sum += i
            self.dfs(cur, k, n, i + 1)
            cur.pop()
            self.sum -= i
    def combinationSum3(self, k, n):
        self.ans = []  # Initialize the answer list
        self.sum = 0   # Initialize the sum
        self.dfs([], k, n, 1)  # Start DFS with an empty current combination list
        return self.ans
        
        
        