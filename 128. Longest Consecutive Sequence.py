"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)  # to avoid running duplicated works
        res = 0
        for n in nums:
            if n-1 not in nums:
                length = 1
                while n+1 in nums:
                    length += 1
                    n += 1
                res = max(res, length)
        return res


"""Sol:
1.check whether the number is start of the sequence and continue. if not do nothing
2. Use set to avoid duplicate works"""
