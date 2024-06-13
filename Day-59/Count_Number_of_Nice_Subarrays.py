'''Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16'''


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        i = 0
        j = 0
        temp = 0
        ans = 0
        while(j<len(nums)):

            if nums[j]%2!=0:
                temp+=1
                count = 0

            if temp==k:
                while(nums[i]%2==0):
                    count+=1
                    i+=1
                count+=1
                i+=1
                temp-=1
            
            ans +=count
            j+=1

        return ans