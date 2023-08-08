"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeLength = n
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for n, d, w in times:
            adj[n].append([d, w])
        shortestPath = {}
        minHeap = [[0, k]]
        while minHeap:
            w1, n = heapq.heappop(minHeap)
            if n in shortestPath:
                continue
            shortestPath[n] = w1
            for d, w2 in adj[n]:
                if d not in shortestPath:
                    heapq.heappush(minHeap, [(w1+w2), d])

        return max(shortestPath.values()) if len(shortestPath) == nodeLength else -1
