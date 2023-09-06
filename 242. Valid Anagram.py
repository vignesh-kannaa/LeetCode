"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1: hashmap
        # if len(s)!= len(t):
        #     return False
        # count_s , count_t = {} ,{}
        # for c in s:
        #     count_s[c] = 1+ count_s.get(c,0)
        # for c in t:
        #     count_t[c] = 1+ count_t.get(c,0)
        # return count_s == count_t

        # solution 2: sort (to reduce space)
        return sorted(s) == sorted(t)
