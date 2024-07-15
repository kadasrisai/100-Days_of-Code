''' Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST. '''

class Solution(object):
    def maxSumBST(self, root):
        def dfs(node, curr_min, curr_max):
            if not node:
                return True, 0, curr_min, curr_max

            left, right, total_sum = True, True, node.val
            l_min, l_max, r_min, r_max = curr_min, curr_max, curr_min, curr_max

            if node.left:
                l_bst, l_sum, l_min, l_max = dfs(node.left, float('inf'), float('-inf'))
                left = l_bst and node.val > max(l_max, l_min)
                total_sum += l_sum

            if node.right:
                r_bst, r_sum, r_min, r_max = dfs(node.right, float('inf'), float('-inf'))
                right = r_bst and node.val < min(r_max, r_min)
                total_sum += r_sum

            if left and right:
                self.best = max(self.best, total_sum)

            is_bst = left and right
            t_min = min(l_min, r_min, node.val)
            t_max = max(l_max, r_max, node.val)
            return is_bst, total_sum, t_min, t_max

        self.best = 0
        dfs(root, root.val, root.val)
        return self.best
