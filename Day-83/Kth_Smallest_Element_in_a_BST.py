''' Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3 '''


class Solution(object):
    
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        self.inorderTraversal(root, k)
        return self.result
    
    def inorderTraversal(self, node, k):
        if not node or self.count >= k:
            return
        
        self.inorderTraversal(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        
        self.inorderTraversal(node.right, k)
        