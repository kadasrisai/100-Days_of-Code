'''  Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph '''

from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        in_degree = [0] * V
        
        # Calculate in-degree of each vertex
        for i in range(V):
            for neighbor in adj[i]:
                in_degree[neighbor] += 1

        # Initialize queue and topo list
        queue = deque()
        topo = []

        # Enqueue all vertices with in-degree 0
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
                topo.append(i)

        # Process the vertices in topological order
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    topo.append(neighbor)

        # If topo list size is not equal to number of vertices, graph has a cycle
        return not (len(topo) == V)