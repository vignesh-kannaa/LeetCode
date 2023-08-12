"""Given two strings s and t, return the number of distinct 
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            if s[i] == t[j]:
                mem[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                mem[(i, j)] = dfs(i+1, j)
            return mem[(i, j)]
        return dfs(0, 0)


""""
LCS
1. track on s
2. only if t completes => 1 , if s completes => 0 eg: s ="" t ="a"
3. even if equal it can be equal to next element so incrementing s 
 """
