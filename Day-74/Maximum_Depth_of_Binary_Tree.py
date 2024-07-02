''' Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2 '''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        # Find depth of left subtree
        left = self.maxDepth(root.left)
        
        # Find depth of right subtree
        right = self.maxDepth(root.right)
        
        # Return depth of current node
        return 1 + max(left, right)