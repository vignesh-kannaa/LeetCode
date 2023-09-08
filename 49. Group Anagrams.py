"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to handle if keys may not exist,providing empty list as default val
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                # calculate position by using ascii values
                count[ord(ch) - ord('a')] += 1

            res[tuple(count)].append(s)  # hashmap doesnot accept list as key
        return res.values()


"""sol:
use hashap with key as 26 character values
"""
