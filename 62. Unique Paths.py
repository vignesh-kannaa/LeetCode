class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0]*n for i in range(m)]

        def memoization(r, c, cache):

            if r >= m or c >= n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m-1 and c == n-1:
                return 1
            cache[r][c] = memoization(
                r+1, c, cache) + memoization(r, c+1, cache)
            return cache[r][c]
        return memoization(0, 0, cache)
