"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 Example 1:
 Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
"""


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        premap = {}
        res = []
        for i in range(numCourses):
            adj[i] = []
        for n, d in prerequisites:
            adj[n].append(d)
        # print('adj: ', adj)

        def dfs(n):
            if n not in premap:
                premap[n] = set()
                for node in adj[n]:
                    premap[n] |= dfs(node)
            premap[n].add(n)
            return premap[n]

        for i in range(len(adj)):
            dfs(i)
        # print('premap: ',premap)
        for n1, n2 in queries:
            res.append(n2 in premap[n1])
        return res


"""
Topological concept
1. use hashmap to save respective flows
2. use set in hashmap to save memory"""
