''' Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.

Example 1:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: 
Yes
Explanation: 
There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.
Example 2:

Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: 
No
Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical. '''

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.data!=root2.data:
            return False
        return self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)

