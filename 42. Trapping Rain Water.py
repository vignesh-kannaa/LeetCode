"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        maxLeft = height[L]
        maxRight = height[R]
        curUnit = 0
        while L < R:
            if maxLeft < maxRight:
                L += 1
                maxLeft = max(maxLeft, height[L])
                curUnit += maxLeft - height[L]
            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                curUnit += maxRight - height[R]
        return curUnit


"""
use 2 pointers
formula: currentUnit += maxLeft-height[L]
move pointers based on max values of left or right
"""
