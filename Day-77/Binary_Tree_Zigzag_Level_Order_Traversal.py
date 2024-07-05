''' Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: [] '''

class Solution(object):
    def zigzagLevelOrder(self, root):
        result=[]
        if not root:
            return []
        queue = [root]
        level=0
        while queue:
            rev = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                rev.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level%2:
                result.append(rev[::-1])
            else: 
                result.append(rev)
            level += 1
        return result