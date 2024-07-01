''' Given a binary tree, find if it is height balanced or not.  A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree. 

Examples:

Input:
      1
    /
   2
    \
     3 
Output: 0
Explanation: The max difference in height of left subtree and right subtree is 2, which is greater than 1. Hence unbalanced
Input:
       10
     /   \
    20   30 
  /   \
 40   60
Output: 1
Explanation: The max difference in height of left subtree and right subtree is 1. Hence balanced. '''

class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
    
    def isBalanced(self,root):
        #add code here
        if root == None:
            return True
        if (abs(self.height(root.left)-self.height(root.right))<=1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False