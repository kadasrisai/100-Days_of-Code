''' Given a Binary Search Tree. Convert a given BST into a Special Max Heap with the condition that all the values in the left subtree of a node should be less than all the values in the right subtree of the node. This condition is applied on all the nodes in the so converted Max Heap.

Example 1:

Input :
                 4
               /   \
              2     6
            /  \   /  \
           1   3  5    7  

Output : 1 2 3 4 5 6 7 
Exaplanation :
               7
             /   \
            3     6
          /   \  /   \
         1    2 4     5
The given BST has been transformed into a
Max Heap and it's postorder traversal is
1 2 3 4 5 6 7.  '''

class Solution:
    def inorder(self,root,lis):
        if root==None:
            return
        self.inorder(root.left,lis)
        lis.append(root.data)
        self.inorder(root.right,lis)
    def solve(self,root,lis):
        if root==None:
            return
        
        self.solve(root.left,lis)
        self.solve(root.right,lis)
        root.data=lis.pop()
        
        
        
        
    def convertToMaxHeapUtil(self, root):
        lis=[]
        self.inorder(root,lis)
        
        lis=lis[::-1]
        self.solve(root,lis)
        return root