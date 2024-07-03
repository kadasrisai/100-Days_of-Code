''' Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1'''


class Solution:
    def lowestCommonAncestor(self,root, p, q):
        if root is None: return None

        if root == p or root == q:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            return root
            
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None: return root
        if left is not None and left == root.left: return left
        if right is not None and right == root.right : return right
        if left is not None: return left
        if right is not None: return right