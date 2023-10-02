"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # default value if there are no increasing temp
        res = [0] * len(temperatures)
        stack = []  # [temp, index]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i-stackInd
            stack.append([temp, i])
        return res

        """
        monotonic decreasing stack => val in stack will be in decreasing format
        stack => [temp, index]
        check the new value with last value in the stack and update in the result"""
