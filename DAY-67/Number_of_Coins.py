''' Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 
Explanation: Use one 6 cent coin
and one 5 cent coin '''

class Solution:
	def minCoins(self, coins, M, V):
		# code here
		dp=[V+1] * (V+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin, V+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return dp[V] if dp[V]!=V+1 else -1