''' The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. The diagram below shows two trees each with diameter nine, the leaves that form the ends of the longest path are shaded (note that there is more than one path in each tree of length nine, but no path longer than nine nodes). 



Example 1:

Input:
       1
     /  \
    2    3
Output: 3
Example 2:

Input:
         10
        /   \
      20    30
    /   \ 
   40   60
Output: 4'''

class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update the diameter if the path through the root of this subtree is larger
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of the tree rooted at this node
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter+1

