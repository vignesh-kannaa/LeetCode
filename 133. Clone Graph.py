"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNode = {}

        def dfs(node):
            if node in oldNode:
                return oldNode[node]
            cur = Node(node.val)
            oldNode[node] = cur
            for n in node.neighbors:
                cur.neighbors.append(dfs(n))
            return cur
        return dfs(node) if node else None
