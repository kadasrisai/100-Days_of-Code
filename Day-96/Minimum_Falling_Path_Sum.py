''' Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown. '''

class Solution(object):
    def minFallingPathSum(self, matrix):
        # initialize dp
        dp = [[0] * len(matrix) for i in range(len(matrix))]
        
		# copy first row as it is in the dp
        for i in range(len(dp[0])):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, len(dp)):
            for j in range(len(dp)):
				# check the three(or available) values from the previous row
                l = dp[i - 1][j - 1] if j > 0 else float('inf')
                u = dp[i - 1][j]
                r = dp[i - 1][j + 1] if j < len(dp[i]) - 1 else float('inf')
				
				# make dp[i][j] the min of the values
                dp[i][j] = min(l, u, r) + matrix[i][j]
        
        return min(dp[-1])