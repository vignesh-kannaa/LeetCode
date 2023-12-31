"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(i):
            if i == len(nums):
                return [[]]
            arr = []
            perm = permutation(i+1)
            for p in perm:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    arr.append(pcopy)
            return arr
        return permutation(0)
