''' Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \      
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \      
                 10       14

For the above tree the output should be 5 10 4 14 25.

Note: The Input/Output format and Example given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.
 

Example 1:

Input:
       1
     /   \
    3     2
Output: 3 1 2
Explanation:
First case represents a tree with 3 nodes
and 2 edges where root is 1, left child of
1 is 3 and right child of 1 is 2.

Thus nodes of the binary tree will be
printed as such 3 1 2.
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 40 20 60 30'''

class Solution:
    def bottomView(self, root):
        mp = {} #-> to keep the track of the level we are on
        queue = []
        queue.append((root,0))
        
        
        while len(queue)>0: # simple BFS
            node,vertical = queue.pop(0)
            
            mp[vertical] = node.data # Each time you come to a vertical, update it
            if node.left:
                queue.append((node.left,vertical-1))
            if node.right:
                queue.append((node.right,vertical+1))
        
        ans = []
        for key in sorted(mp.keys()): #-> need to sort keys in python, as dict doesn't sort by default
            ans.append(mp[key])
        
        return ans