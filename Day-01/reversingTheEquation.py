'''Given a mathematical equation that contains only numbers and +, -, *, /. 
Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros. '''

class Solution:
    def reverseEqn(self, s):
        # code here
        ans=''
        ans1=''
        for i in s:
            if i in ['+','-','*','/']:
                ans=ans1+ans
                ans=i+ans
                ans1=''
            else:
                ans1+=i
        ans=ans1+ans    
        return ans