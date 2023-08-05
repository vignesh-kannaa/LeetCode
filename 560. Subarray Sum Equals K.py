"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDic = {0: 1}
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            sums = prefix-k
            if sums in prefixDic:
                res += prefixDic[sums]
            prefixDic[prefix] = prefixDic.get(prefix, 0)+1

        return res


"""
Sol:
use prefix with dictionary 
Validate sum = prefix - k is in dictionary
"""
