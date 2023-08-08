"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation(i):
            if i == len(nums):
                return [[]]
            arr = []
            perm = permutation(i+1)
            for p in perm:
                for j in range(len(p)+1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    if pcopy not in arr:
                        arr.append(pcopy)
            return arr
        return permutation(0)
