''' Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.


Example 1:

Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()
Example 2:
Input:
N = 1
Output:
()'''
class Solution:
    def AllParenthesis(self,n):
        #code here
        res = []
        def dfs(s,open,close):
            if len(s) == n*2:
                res.append(s)
                return
            if open <n:
                dfs(s+'(',open+1,close)
            if close<open:
                dfs(s+')',open,close+1)
        dfs('',0,0)
        return res