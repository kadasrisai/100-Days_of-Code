''' Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

Example 2:

Input:


Output: 0
Explanation: no cycle in the graph
 '''

 from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        color = {}
        parent = {}

        for node in range(V):
            color[node] = "W"
            parent[node] = None

        def dfs(u, color, parent):
            color[u] = 'G'

            for v in adj[u]:
                if color[v] == "W":
                    if dfs(v, color, parent):
                        return True
                elif color[v] == "G":
                    return True

            color[u] = "B"
            return False

        for u in range(V):
            if color[u] == "W":
                if dfs(u, color, parent):
                    return True

        return False