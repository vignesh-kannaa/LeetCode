class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax = globMin = nums[0]
        curMax = curMin = total = 0
        for n in nums:
            curMax = max(n, curMax+n)
            curMin = min(n, curMin+n)
            total += n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)
        return max(total - globMin, globMax) if globMax > 0 else globMax

# Kadane's algorithm
# edge case: if all are negative, total - globMin will be 0. comparing 0, glbomax(negative value) will return 0. so use it is different case
