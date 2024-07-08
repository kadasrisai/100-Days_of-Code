'''Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
 Example 1:

Input:
      1
    /   \
   2     3
Output: 
1 2 3
Explanation:
The converted BST will be 
      2
    /   \
   1     3

Example 2:

Input:
          1
       /    \
     2       3
   /        
 4       
Output: 
1 2 3 4
Explanation:
The converted BST will be

        3
      /   \
    2     4
  /
 1  '''


 class Solution:
    def inorder(self, root, v):
        if not root:
            return
        self.inorder(root.left, v)
        v.append(root.data)
        self.inorder(root.right, v)
        
    def fill_it(self, root, v, ind):
        if not root:
            return
        self.fill_it(root.left, v, ind)
        root.data = v[ind[0]]
        ind[0]+=1
        self.fill_it(root.right, v, ind)
        
    def binaryTreeToBST(self, root):
        # code here
        v = []
        self.inorder(root, v) 
        
        v.sort() 
        ind = [0]
       
        self.fill_it(root, v, ind) 
        return root
