"""Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr, subarr = [], []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                arr.append(subarr.copy())
                return
            #  include
            subarr.append(nums[i])
            dfs(i+1)
            # not include
            subarr.pop()
            # skip all the duplicates
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1)
        dfs(0)
        return arr


"""sol: 
1. backtracking include and not include elements
2. use sort and while loop to skip the duplicate being added
"""
