'''Given an array Arr consisting of N distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1:

Input: 
N = 4 
arr[] = {1, 5, 3, 2}
Output: 2 
Explanation: There are 2 triplets:
 1 + 2 = 3 and 3 +2 = 5

Example 2:

Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits '''

class Solution:
	def countTriplet(self, arr, n):
		# code here
		array = set(arr)
        count = 0
        for i in range(n-1):
            for j in range(i+1,n):
                summ = arr[i]+arr[j]
                if (summ in array):
                    count += 1
        return count
