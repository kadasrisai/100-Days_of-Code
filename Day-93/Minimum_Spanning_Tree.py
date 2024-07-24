''' Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing pairs of integers. Each pair represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

Example 1:

Input:
3 3
0 1 5
1 2 3
0 2 1

Output:
4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Example 2:

Input:
2 1
0 1 5

Output:
5
Explanation:
Only one Spanning Tree is possible
which has a weight of 5. '''

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        #        kruskal algorithm
        def find(a):
            while a!=pr[a]:
                a=pr[a]
            return a
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return False
            if sz[a]>sz[b]:
                a,b=b,a
            pr[a]=b
            sz[b]+=sz[a]
            return True
        pr=[*range(V)]
        sz=[1]*V
        
        edges=[]
        for fm,edge in enumerate(adj):
            for to,ct in edge:
                edges.append((ct,fm,to,))
        edges.sort()
        
        ret=0
        for ct,fm,to in edges:
            if find(fm)!=find(to):
                ret+=ct
                union(fm,to)
        return ret