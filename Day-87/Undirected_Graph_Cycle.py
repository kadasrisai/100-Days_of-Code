''' Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:

Input:  
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
Example 2:

Input: 
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation: 

No cycle in the graph. '''

from typing import List
from collections import deque, defaultdict

class Solution:
    #Function to detect cycle in an undirected graph.
    def cyclicBfs(self, node, adj, visited):
        parent = {}
        queue = deque([node])
        
        visited[node] = True
        parent[node] = -1
        
        while queue:
            frontNode = queue.popleft()
            
            for neighbor in adj[frontNode]:
                if visited[neighbor] and parent[frontNode] != neighbor:
                    return True
                elif not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = frontNode
        
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if self.cyclicBfs(i, adj, visited):
                    return True
        
        return False
