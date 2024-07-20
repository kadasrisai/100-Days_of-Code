''' Given an adjacency list for a Directed Acyclic Graph (DAG) where adj_list[i] contains a list of all vertices j such that there is a directed edge from vertex i to vertex j, with  V  vertices and E  edges, your task is to find any valid topological sorting of the graph.

 

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
    
    def dfs (self,src,visited,st,adj):
        visited[src]=1
        for i in adj[src]:
            if not visited[i]:
                self.dfs(i,visited,st,adj)
                
        st.append(src) 
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        visited=[0]*V
        st=[]
        ans=[]
        for i in range(V):
            if  not visited[i]:
                self.dfs(i,visited,st,adj)
                
        while st:
            ans.append(st.pop())
            
        return ans   
