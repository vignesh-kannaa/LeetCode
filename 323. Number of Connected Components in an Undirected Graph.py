"""In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

You need to return the number of connected components in that graph.


Example
Example 1

Input:

3
[[0,1], [0,2]]
Output:

1
Example 2

Input:

6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:

2"""

from typing import (
    List,
)


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for n in adj[node]:
                dfs(n)
        res = 0
        for i in adj:
            if i not in visit:
                res += 1
                dfs(i)

        return res
