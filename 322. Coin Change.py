"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(i, curamount):
            if i >= len(coins):
                return float('inf')
            if (i, curamount) in mem:
                return mem[(i, curamount)]
            if curamount == amount:
                return 0

            skipcurrent = dfs(i+1, curamount)
            if curamount + coins[i] <= amount:
                includecurrent = 1+dfs(i, curamount + coins[i])
            else:
                includecurrent = float('inf')

            mem[(i, curamount)] = min(skipcurrent, includecurrent)
            return mem[(i, curamount)]
        res = dfs(0, 0)
        return -1 if res == float('inf') else res


"""Subset with target and its unlimited so DP - unbounded knapsack"""
