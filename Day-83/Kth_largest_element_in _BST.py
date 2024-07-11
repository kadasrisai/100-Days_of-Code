''' Given a Binary Search Tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.

Example 1:

Input:
      4
    /   \
   2     9
k = 2 
Output: 4
Example 2:

Input:
       9
        \ 
          10
K = 1
Output: 10 '''

class Solution:
    def inOrder(self,root,ans):
        if not root:
            return 
        self.inOrder(root.left,ans)
        ans.append(root.data)
        self.inOrder(root.right,ans)
    
    def kthLargest(self,root, k):
        ans=[]
        self.inOrder(root,ans)
        ans.reverse()
        return ans[k-1]
        