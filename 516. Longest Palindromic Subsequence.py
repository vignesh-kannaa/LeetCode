"""Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def longestCommonSubsequence(text1: str, text2: str) -> int:
            prevrow = [0] * (len(text2)+1)
            for i in range(len(text1)-1, -1, -1):
                currow = [0] * (len(text2)+1)
                for j in range(len(text2)-1, -1, -1):
                    if text1[i] == text2[j]:
                        currow[j] = 1 + prevrow[j+1]
                    else:
                        currow[j] = max(currow[j+1], prevrow[j])
                prevrow = currow
            return prevrow[0]

        return longestCommonSubsequence(s, s[::-1])


"""reverse the given input and provide as 2nd input to lcs"""
