'''Given a Binary Search Tree that contains unique positive integer values greater than 0. The task is to complete the function isDeadEnd which returns true if the BST contains a dead end else returns false. Here Dead End means a leaf node, at which no other node can be inserted.

Example 1:

Input :   
               8
             /   \ 
           5      9
         /  \     
        2    7 
       /
      1     
          
Output : 
Yes
Explanation : 
Node 1 is a Dead End in the given BST.
Example 2:

Input :     
              8
            /   \ 
           7     10
         /      /   \
        2      9     13

Output : 
Yes
Explanation : 
Node 9 is a Dead End in the given BST. '''

class Solution:
    def isDeadEnd(self, root):
        # Code here
        nodes = set()
        leafs = set()
        if root == None:
            return False
        def Allnodes(root,nodes,leafs):
            
            if (root == None):
                return
            nodes.add(root.data)
            
            if (root.left == None and root.right == None):
                leafs.add(root.data)
                return
            Allnodes(root.left,nodes,leafs)
            Allnodes(root.right,nodes,leafs)
        Allnodes(root,nodes,leafs)
        
        for i in leafs:
            if ((i+1) in nodes) and ((i-1) in nodes):
                return True
            elif i == 1 :
                if 2 in nodes:
                    return True
        return False
