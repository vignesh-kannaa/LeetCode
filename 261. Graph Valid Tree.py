"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example
Example 1:

Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.
Example 2:

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""
from typing import (
    List,
)


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        if not n:
            return True
        for i in range(n):
            adj[i] = []
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for n in adj[i]:
                if n == prev:
                    continue
                if not dfs(n, i):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
