"""You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
Example 2:

Input: stones = [31,26,33,21,40]
Output: 5"""


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = ceil(totalSum/2)
        mem = {}
        result = max(stones)

        def dfs(i, w):
            if w >= target or i >= len(stones):
                # sum - target gives remaining half
                return abs(w - (totalSum - w))
            if (i, w) in mem:
                return mem[(i, w)]
            mem[(i, w)] = min(dfs(i+1, stones[i]+w), dfs(i+1, w))
            return mem[(i, w)]
        return dfs(0, 0)


"""
try to create a two stones with half the total weight so that the output is minimum
now one is the target and use bounded knapsack
target = ceil(sum(stones)/2)
Remaining can be caluclated using sum - target"""
