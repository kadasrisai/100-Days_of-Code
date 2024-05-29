''' Given an infix expression in the form of string str. Convert this infix expression to postfix expression.

Infix expression: The expression of the form a op b. When an operator is in-between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The order of precedence is: ^ greater than * equals to / greater than + equals to -. Ignore the right associativity of ^.
Example 1:

Input: str = "a+b*(c^d-e)^(f+g*h)-i"
Output: abcd^e-fgh*+^*+i-
Explanation:
After converting the infix expression 
into postfix expression, the resultant 
expression will be abcd^e-fgh*+^*+i-'''
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        ans =""
        stack=[]
        dic={'^':3  , '*':2, '/':2, '+':1, '-':1}
        
        for i in  exp :
            if i.isalnum():
                ans += i  
            
            elif i =='(':
                stack.append(i)
            
            elif i == ')': 
                while stack and stack[-1] != '(':
                    ans+= stack.pop()
                stack.pop()
            else : 
                while stack and dic.get(stack[-1], 0) >= dic[i]:
                    ans += stack.pop()
                stack.append(i)
            
        while stack :
            ans += stack.pop()
            
        return ans
