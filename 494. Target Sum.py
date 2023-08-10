"""You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        def dfs(i, curSum):
            if i >= len(nums):
                if curSum == target:
                    return 1
                return 0
            if (i, curSum) in mem:
                return mem[(i, curSum)]
            mem[(i, curSum)] = dfs(i+1, curSum-nums[i]) + \
                dfs(i+1, curSum + nums[i])
            return mem[(i, curSum)]
        return dfs(0, 0)


"""dynamic programming:
recursion with memoization """
