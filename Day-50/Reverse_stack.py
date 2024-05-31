''' You are given a stack St. You have to reverse the stack using recursion.

Example 1:

Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}
Explanation:
Input stack after reversing will look like the stack in the output.
Example 2:

Input:
St = {4,3,9,6}
Output:
{6,9,3,4}
Explanation:
Input stack after reversing will look like the stack in the output.'''

from typing import List

class Solution:
    def reverse(self,s): 
        #code here
        def helper(s,n,i):
            if i>=(n//2):
                return
            s[i],s[n-1-i]=s[n-1-i],s[i]
            helper(s,n,i+1)
        helper(s,len(s),0)