''' 
Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   '''

class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        else:
            leftdepth = self.height(root.left)
            rightdepth = self.height(root.right)
            
        return 1 + max(leftdepth,rightdepth)