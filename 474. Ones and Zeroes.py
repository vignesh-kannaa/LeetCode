"""You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2."""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        mem = {}

        def dfs(i, czero, cones):
            if i >= len(strs):
                return 0
            if (i, czero, cones) in mem:
                return mem[(i, czero, cones)]
            if czero+strs[i].count('0') <= m and strs[i].count('1')+cones <= n:
                mem[(i, czero, cones)] = max(1 + dfs(i+1, czero+strs[i].count('0'),
                                                     cones+strs[i].count('1')), dfs(i+1, czero, cones))
            else:
                mem[(i, czero, cones)] = dfs(i+1, czero, cones)
            return mem[(i, czero, cones)]
        return dfs(0, 0, 0)


"""
Dynamic programming with memoization
add 1 at the time of calling the recursion to add that current subset
get max value since there are many subsets with correct ans
"""
