""" Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval = nums[0]
        curval = 0
        for n in nums:
            curval = max(0, curval)
            curval += n
            maxval = max(maxval, curval)
        return maxval


"""Solution: using Kadane's algorithm"""
