'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[] # maintain the monotonically decresing heights 
        ans=0
        for i in range(0,len(height)):        
            while stack!=[] and height[stack[-1]]<=height[i]: # check if their is any larger height than last smaller height encountered so far in stack
                temp=stack.pop()
                if stack!=[]:
                    h=min(height[stack[-1]],height[i])-height[temp]
                    w=i-stack[-1]-1
                    ans+=h*w
            stack.append(i)
        return ans
        