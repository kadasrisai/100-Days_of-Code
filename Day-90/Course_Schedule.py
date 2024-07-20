''' There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def dfs(sv,visited,path):
            visited[sv]=1
            path[sv]=1
            for u in adj[sv]:
                if visited[u]==0:
                    if dfs(u,visited,path):
                        return True
                elif path[u]==1:
                    return True
            path[sv]=0
            return False
        
        adj=[[] for i in range(numCourses)]
        n=len(prerequisites)
        for i in range(n):
            u,v=prerequisites[i][0],prerequisites[i][1]
            adj[v].append(u)
        visited=[0]*numCourses
        path=[0]*numCourses
        for i in range(numCourses):
            if visited[i]==0:
                if dfs(i,visited,path):
                    return False
        return True