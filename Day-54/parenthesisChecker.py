''' Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Example 1:

Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.
Example 2:

Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.'''

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = []
        for char in x:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top == '(' and char != ')') or \
                   (top == '[' and char != ']') or \
                   (top == '{' and char != '}'):
                    return False
        return len(stack) == 0
        