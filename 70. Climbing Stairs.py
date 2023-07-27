class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        d = [1, 2]
        i = 3
        while i <= n:
            temp = d[1]
            d[1] = d[1]+d[0]
            d[0] = temp
            i += 1
        return d[1]
