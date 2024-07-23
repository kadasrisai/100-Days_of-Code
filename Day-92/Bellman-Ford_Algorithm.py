''' Given a weighted and directed graph of V vertices and E edges, Find the shortest distance of all the vertex's from the source vertex S. If a vertices can't be reach from the S then mark the distance as 10^8. Note: If the Graph contains a negative cycle then return an array consisting of only -1.

Example 1:

Input:

E = [[0,1,9]]
S = 0
Output:
0 9
Explanation:
Shortest distance of all nodes from
source is printed.
Example 2:

Input:

E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
Output:
1 6 0
Explanation:
For nodes 2 to 0, we can follow the path-
2-0. This has a distance of 1.
For nodes 2 to 1, we cam follow the path-
2-0-1, which has a distance of 1+5 = 6, '''


class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        # Initialize the price array with a large positive number
        prices = [10**8] * V
        prices[S] = 0

        # Relaxation step
        for i in range(V - 1):
            for source, destination, cost in edges:
                if prices[source] != 10**8 and prices[destination] > prices[source] + cost:
                    prices[destination] = prices[source] + cost

        # Check for negative-weight cycles
        for source, destination, cost in edges:
            if prices[source] != 10**8 and prices[destination] > prices[source] + cost:
                return [-1]  # Indicating the presence of a negative-weight cycle

        return prices