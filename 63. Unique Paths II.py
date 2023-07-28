class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        ROWS, COLS = len(grid), len(grid[0])
        cache = [[0]*COLS for i in range(ROWS)]

        def memoization(r, c, cache):
            if r >= ROWS or c >= COLS:
                return 0
            if grid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS-1 and c == COLS-1:
                return 1
            cache[r][c] = memoization(
                r+1, c, cache) + memoization(r, c+1, cache)
            return cache[r][c]
        return memoization(0, 0, cache)
