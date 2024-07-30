'''
Given an array of integers A[] of length N and an integer target.
You want to build an expression out of A by adding one of the symbols '+' and '-' before each integer in A and then concatenate all the integers.

For example, if arr = {2, 1}, you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that can be built, which evaluates to target and return your answer with modulo 109+7.


Example 1:

Input:
N = 5
A[] = {1, 1, 1, 1, 1}
target = 3
Output:
5
Explanation:
There are 5 ways to assign symbols to 
make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input:
N = 1
A[] = {1}
target = 1
Output:
1
 '''

 class Solution:
    def findTargetSumWays(self, n, arr, target):
        # code here 
        memo = {}
        
        def f(arr,target):
            
            state = ( target, tuple(arr) )
            
            if state in memo:
                return memo[state]
            else:
                if target==0 and len(arr)==0:
                    return 1
                if target!=0 and len(arr)==0:
                    return 0
                
                value = f(arr[:-1] , target-arr[-1] ) + f(arr[:-1] , target+arr[-1] )
                memo[state] = value
                
                return value
            
            
        return f(arr,target)