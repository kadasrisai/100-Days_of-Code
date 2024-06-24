'''Given a string S of distinct character of size N and their corresponding frequency f[ ] i.e. character S[i] has f[i] frequency. Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree.
Note: While merging if two nodes have the same value, then the node which occurs at first will be taken on the left of Binary Tree and the other one to the right, otherwise Node with less value will be taken on the left of the subtree and other one to the right.

Example 1:

S = "abcdef"
f[] = {5, 9, 12, 13, 16, 45}
Output: 
0 100 101 1100 1101 111
Explanation:
Steps to print codes from Huffman Tree
HuffmanCodes will be:
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111
Hence printing them in the PreOrder of Binary 
Tree.'''

import heapq
class node:
    def __init__(self, freq, symbol, left=None, right= None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    def __lt__(self,nxt):
        return self.freq < nxt.freq


def getList(ans,node, val = ''):
    
    newval = val + str(node.huff)
    
    if node.left:
        getList(ans, node.left, newval)
    if node.right:
        getList(ans, node.right, newval)
    
    if not node.left and not node.right:
        ans.append(newval)


class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        nodes = []
        for x in range(len(S)):
            heapq.heappush(nodes,node(f[x],S[x]))
        
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            
            left.huff = '0'
            right.huff = '1'
            
            newnode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
            heapq.heappush(nodes, newnode)
        
        ans = []
        getList(ans,nodes[0])
        return ans