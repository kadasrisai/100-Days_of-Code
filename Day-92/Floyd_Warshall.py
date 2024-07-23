''' The problem is to find the shortest distances between every pair of vertices in a given edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there is no edge from i to j.
Note : Modify the distances for every pair in-place.

Examples :

Input: matrix = [[0, 25],[-1, 0]]

Output: [[0, 25],[-1, 0]]

Explanation: The shortest distance between every pair is already given(if it exists).
Input: matrix = [[0, 1, 43],[1, 0, 6],[-1, -1, 0]]

Output: [[0, 1, 7],[1, 0, 6],[-1, -1, 0]]

Explanation: We can reach 2 from 0 as 0->1->2 and the cost will be 1+6=7 which is less than 43.
Expected Time Complexity: O(n3)
Expected Space Complexity: O(1) '''

class Solution:
	def shortest_distance(self, distance):
		#Code here
		n = len(distance)
        for k in range(n): # Via X
            for i in range(n): # u
                for j in range(n): # v
                    if distance[i][j] != -1 and distance[i][k] != -1 and distance[k][j] != -1:
                        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                    else:
                        if distance[i][k] == -1 or distance[k][j] == -1:
                            continue
                        else:
                            distance[i][j] = distance[i][k] + distance[k][j]
