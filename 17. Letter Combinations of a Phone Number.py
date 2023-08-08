"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr, subarr = [], ""
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(i, subarr):
            if len(subarr) == len(digits):
                arr.append(subarr)
                return
            if i >= len(digits):
                return
            for c in d[digits[i]]:
                dfs(i+1, subarr + c)
        if digits:
            dfs(0, '')
        return arr


"""
Sol:
use backtracking with iteration instead of include and not include"""
