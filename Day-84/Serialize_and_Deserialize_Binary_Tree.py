''' Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []  '''

class Codec:

    def serialize(self, root):
        # Initialize an empty list to store serialized node values
        ans = []

        # Define a depth-first search (DFS) function to serialize the tree
        def DFS(root):
            # Base case: If the current node is None, append "N" to represent null node
            if not root:
                ans.append("N")
                return

            # Append the value of the current node to the list
            ans.append(str(root.val))
            
            # Recursively serialize left and right subtrees
            DFS(root.left)
            DFS(root.right)

        # Call the DFS function to serialize the tree
        DFS(root)
        
        # Join the list elements into a string separated by commas and return
        return ",".join(ans)        

    def deserialize(self, data):
        # Split the serialized string into a list of node values
        value = data.split(",")
        
        # Initialize index to keep track of current position in the list
        self.index = 0

        # Define a DFS function to reconstruct the tree from serialized data
        def DFS():
            # If the current value is "N", indicating a null node, return None
            if value[self.index] == "N":
                self.index += 1
                return None

            # Create a new TreeNode with the current value
            root = TreeNode(int(value[self.index]))
            self.index += 1
            
            # Recursively construct left and right subtrees
            root.left = DFS()
            root.right = DFS()
            
            return root

        # Call the DFS function to deserialize the tree and return the root
        return DFS()   
        