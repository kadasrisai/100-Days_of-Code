'''Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument. If no left view is possible, return an empty tree.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Example 2:

Input:

Output: 10 20 40 '''

class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    res= []
    view_left(root, res, 0)
    return res

def view_left(root, res, lvl):
    if root is None:
        return
    if lvl == len(res):
        res.append(root.data)
    view_left(root.left, res, lvl+1)
    view_left(root.right, res, lvl+1)
    