''' Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2). '''


class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        queue = [(root, 0)]
        max_width = 0
        while queue:
            level_size = len(queue)
            left_pos = queue[0][1]
            right_pos = queue[-1][1]
            max_width = max(max_width, right_pos - left_pos + 1)
            for i in range(level_size):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
            # Reset positions to avoid integer overflow
            for i in range(len(queue)):
                queue[i] = (queue[i][0], queue[i][1] - left_pos)
        return max_width
        