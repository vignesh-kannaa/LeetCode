"""Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets."""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)/2
        mem = {}

        def dfs(i, curSum):
            if i >= len(nums) or curSum > target:
                return False
            if (i, curSum) in mem:
                return mem[(i, curSum)]
            if curSum == target:
                return True
            mem[(i, curSum)] = dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum)
            return mem[(i, curSum)]
        return dfs(0, 0)


"""
target = sum/2
sum%2 should be equal
recurssion using memoization
"""
