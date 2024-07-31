'''
Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
Example 2:

Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 
24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 1, i.e, 8*price[1]= 8*3 = 24. '''

class Solution:
    def cutRod(self, price, n):
        #code here
        # Create a DP array to store the maximum profit for each length
        dp = [0] * (n + 1)

        # Build the DP array in bottom-up manner
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(i):
                max_val = max(max_val, price[j] + dp[i - j - 1])
            dp[i] = max_val

        return dp[n]