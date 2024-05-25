'''Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]] '''

 class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        def subset(p, up):
            if len(up) == 0:
                if p not in ans:
                    ans.append(p)
                return 
            ch = up[0]
            for i in range(len(p) + 1):
                subset(p[0:i] + [ch] + p[i:], up[1:])
        subset([], nums)
        return ans