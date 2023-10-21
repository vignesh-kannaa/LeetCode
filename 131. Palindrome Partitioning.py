"""Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 """


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            return True if s == s[::-1] else False

        def backtrack(i, subarr):
            if i >= len(s):
                res.append(subarr.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    subarr.append(s[i:j+1])
                    backtrack(j+1, subarr)
                    subarr.pop()
        backtrack(0, [])
        return res
