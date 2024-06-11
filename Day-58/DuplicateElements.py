'''Remove duplicate elements from sorted Array

EasyAccuracy: 38.18%Submissions: 228K+Points: 2


Be the comment of the day in POTD and win a GfG T-Shirt!
Solve right now

banner
Given a sorted array a[] of size n, delete all the duplicated elements from a[] & modify the array such that only distinct elements should be present there.

Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size where only distinct elements are present in the array, the driver code will print all the elements of the modified array.

Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 
1
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. {2} so modify array will contains 2 at first position and you should return 1 after modify the array.'''
class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		i = 0
        
        for j in range(1, N):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
                
        return i + 1