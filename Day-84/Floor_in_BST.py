''' You are given a BST(Binary Search Tree) with n number of nodes and value x. your task is to find the greatest value node of the BST which is smaller than or equal to x.
Note: when x is smaller than the smallest node of BST then returns -1.

Example:

Input:
n = 7               2
                     \
                      81
                    /     \
                 42       87
                   \       \
                    66      90
                   /
                 45
x = 87
Output:
87
Explanation:
87 is present in tree so floor will be 87.
Example 2:

Input:
n = 4                     6
                           \
                            8
                          /   \
                        7       9
x = 11
Output:
9 '''




class Solution:
    def __init__(self):
        self.floor_value = -1
    def find_floor_value(self, node, target_value):
        # Code here
        if not node:
            return

        if node.data == target_value:
            self.floor_value = target_value
            return

        if node.data < target_value:
            self.floor_value = max(self.floor_value, node.data)
            self.find_floor_value(node.right, target_value)
            
        else:
            self.find_floor_value(node.left, target_value)
            
    def floor(self, root,x):
        self.find_floor_value(root,x)
        return self.floor_value  
