"""Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        maxHeap = []
        q = deque()
        time = 0
        for t in tasks:
            counter[t] = 1 + counter.get(t, 0)

        for v in counter.values():
            heapq.heappush(maxHeap, -v)

        while maxHeap or q:
            time += 1
            if maxHeap:
                # reduce 1 value, since already -ve add 1 value
                count = 1+heapq.heappop(maxHeap)
                if count:
                    # the added count value can be used after cooldown time
                    q.append([count, time+n])
            if q and q[0][1] == time:
                c, t = q.popleft()
                heapq.heappush(maxHeap, c)
        return time


"""
use hashmap, maxHeap, queue
        2) take the maximum count value, reduce 1 from it(meaning 1 task is done)
        add remaining count + next time it can be used
        3) pop queue and if the first value time is equal add back to maxheap"""
