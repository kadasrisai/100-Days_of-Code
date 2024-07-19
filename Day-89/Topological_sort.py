'''
Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.

 

In a topological sort, for every directed edge u -> v,  u must come before v in the ordering.

 

Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0. '''


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        ans = []
        indegree = [0] * V 
        q = []
        
        for i in range(V):
            for x in adj[i]:
                temp = indegree[x]
                temp += 1
                indegree[x] = temp
        
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            u = q.pop(0)
            ans.append(u)
            for x in adj[u]:
                temp = indegree[x]
                temp -= 1
                indegree[x] = temp
                if indegree[x] == 0:
                    q.append(x)
        return ans