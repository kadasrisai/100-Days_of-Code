'''A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        ans = [root.val]  # Initialize a list to store the result

        def DFS(root):
            if root == None:
                return 0  # Base case: return 0 if the node is None

            # Recursive calculation for left and right subtrees
            # Ensure that negative values are not considered (max(0, ...))
            lmax = max(0, DFS(root.left))
            rmax = max(0, DFS(root.right))

            # Update the overall maximum path sum
            ans[0] = max(ans[0] , root.val + lmax + rmax)

            # Return the maximum path sum that starts from the current node
            return root.val + max(lmax , rmax)

        # Call the DFS function on the root node
        DFS(root) 

        # Return the final maximum path sum
        return ans[0]
        



        