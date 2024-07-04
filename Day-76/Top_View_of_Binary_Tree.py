''' Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree and are at same position then consider the left ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100 '''


class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def solve(self,heap,di,c):
        while c!=0:
            t=heap.pop(0)
            c-=1
            root=t[0]
            line=t[1]
            if line not in di:
                di[line]=root.data
            if root.left:
                heap.append([root.left,line-1])
                c+=1
            if root.right:
                heap.append([root.right,line+1])
                c+=1
            ans=[]
        for i in di:
            ans.append([i,di[i]])
        ans.sort(key=lambda x:x[0])
        p=[]
        for i in ans:
            p.append(i[1])
        return p
        
    def topView(self,root):
        if root is None:
            return []
        else:
            di=OrderedDict()
            return self.solve([[root,0]],di,1)