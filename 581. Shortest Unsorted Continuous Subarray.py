"""Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # two solution:
        # 1. sort and compare the values of mismatch
        # sort = sorted(nums)
        # start = len(nums)-1
        # end = 0
        # for i,n in enumerate(nums):
        #     if sort[i] != n:
        #         start = min(start,i)
        #         end = max(end, i)
        # return (end-start)+1 if (end - start) > 0 else 0
        # 2. index element should be > left values and should be < right values
        maxval, end = nums[0], 0
        minval, start = nums[-1], len(nums)-1

        for i in range(1, len(nums)):  # find val that breaks sorting
            if nums[i] >= maxval:
                maxval = nums[i]
            else:
                end = i

        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= minval:
                minval = nums[i]
            else:
                start = i
        return (end-start)+1 if (end - start) > 0 else 0
