''' You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.'''

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        st = []
        ans = ''
        for i in range(len(pre_exp)-1,-1,-1):
            c = pre_exp[i]
            if( c.isalpha()):
                st.append(c)
                
            else:
                s1 = st.pop()
                s2 = st.pop()
                res = '('+s1+c+s2+')'
                st.append(res)
                
        return st[-1] 