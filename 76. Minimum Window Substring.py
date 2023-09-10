"""Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string."""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '':
            return ''
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        print(countT)
        L = 0
        res = ''
        resLen = float('inf')
        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if R-L+1 < resLen:
                    res = s[L:R+1]
                    resLen = R-L+1
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        return res


"""SOL: sliding window
2 dictionary
2 variables to check overall condition"""
