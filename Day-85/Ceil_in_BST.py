''' Given a BST and a number X, find Ceil of X.
Note: Ceil(X) is a number that is either equal to X or is immediately greater than X.

If Ceil could not be found, return -1.

Example 1:

Input:
      5
    /   \
   1     7
    \
     2 
      \
       3
X = 3
Output: 3
Explanation: We find 3 in BST, so ceil
of 3 is 3.
Example 2:

Input:
     10
    /  \
   5    11
  / \ 
 4   7
      \
       8
X = 6
Output: 7
Explanation: We find 7 in BST, so ceil
of 6 is 7. '''

class Solution:
    def dfs(self,root,arr):
        
        if root is None:
            return 0
        self.dfs(root.left,arr)
        arr.append(root.key)
        self.dfs(root.right,arr)
        
    def findCeil(self,root, inp):
        # code here
        arr = []
        self.dfs(root,arr)
        for i in range(len(arr)):
            arr[i] = arr[i] - inp
        val = 1 + 10**5
        for i in range(len(arr)):
            if arr[i] > -1 and arr[i] < val:
                val = arr[i]
        if val == 1 + 10**5:
            return(-1)
        else:
            return(val+inp)