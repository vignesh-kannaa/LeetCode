"""There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
You may assume all letters are in lowercase.
The dictionary is invalid, if string a is prefix of string b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order.
The letters in one string are of the same rank by default and are sorted in Human dictionary order.

Example 1:

Input: ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Explanation:
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"


Example 2:

Input: ["z","x"]
Output:"zx"
Explanation:
from "z" and "x", we can get 'z' < 'x'
So return "zx"
"""
from typing import List


class Solution:
    def alienOrder(self, words: List[int]) -> str:
        adj = {}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = []

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        print(adj)
        visit = set()
        path = set()
        res = []

        def dfs(n):
            if n in path:
                return True
            if n in visit:
                return False
            visit.add(n)
            path.add(n)
            for i in adj[n]:
                r = dfs(i)
                if r:
                    return True
            path.remove(n)
            res.append(n)
            return False
        for ch in adj:
            if dfs(ch):
                return ''
        res.reverse()
        result = ''
        for r in res:
            result += r
        return result


words = ["wrt", "wrf", "er", "ett", "rftt"]
sol = Solution()
print(sol.alienOrder(words))
